from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools
import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, WebsiteSearchTool


load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


groq_api_key = os.environ["GROQ_API_KEY"]
# groq_api_key = st.secrets["GROQ_API_KEY"]

# tools
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()


class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(
            model="openai/gpt-3.5-turbo", max_tokens=4000, temperature=0.2
        )
        self.groq = ChatGroq(
            temperature=0, groq_api_key=groq_api_key, model="groq/llama3-8b-8192"
        )

        # Instantiate the tools
        # self.search_tool = SearchTools().search_internet
        self.calculator_tool = CalculatorTools().calculate

    def expert_travel_agent(self):
        return Agent(
            role="Agente de Viagens Especialista",
            backstory=dedent(
                """Especialista em planejamento e logística de viagens.\nTenho décadas de experiência criando roteiros de viagem."""
            ),
            goal=dedent("""
                        Crie um roteiro de viagem de 7 dias com planos detalhados por dia,\n incluindo orçamento, sugestões de bagagem e dicas de segurança.\nIMPORTANTE: Todas as respostas devem ser em português do Brasil.
                        """),
            tools=[search_tool, web_rag_tool],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="Especialista em Seleção de Cidades",
            backstory=dedent(
                """Especialista em analisar dados de viagem para escolher os destinos ideais"""
            ),
            goal=dedent(
                """Selecionar as melhores cidades com base no clima, estação, preços e interesses do viajante.\nIMPORTANTE: Todas as respostas devem ser em português do Brasil."""
            ),
            tools=[search_tool, web_rag_tool],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def local_tour_guide(self):
        return Agent(
            role="Guia Turístico Local",
            backstory=dedent("""Guia local experiente com amplo conhecimento sobre a cidade, suas atrações e costumes"""),
            goal=dedent("""Fornecer as MELHORES informações sobre a cidade selecionada.\nIMPORTANTE: Todas as respostas devem ser em português do Brasil."""),
            tools=[search_tool, web_rag_tool],
            verbose=True,
            llm=self.OpenAIGPT35,
        )
