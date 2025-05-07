import streamlit as st
from main import TripCrew
from fpdf import FPDF
import base64

st.title("Bem-vindo ao Trip Planner Crew")

with st.sidebar:
    st.header("Informe os detalhes da sua viagem")
    topic = "Crie um roteiro de viagem de 7 dias com planos detalhados por dia, incluindo orçamento, sugestões de bagagem e dicas de segurança."
    origin = st.text_input("De onde você vai viajar?")
    cities = st.text_input(
        "Quais cidades você tem interesse em visitar?"
    )
    date_range = st.text_input(
        "Qual o período da sua viagem?"
    )
    interests = st.text_input("Quais são seus principais interesses e hobbies?")

roteiro = None
if st.button("Gerar roteiro"):
    if not topic or not origin or not cities or not date_range or not interests:
        st.error("Por favor, preencha todos os campos.")
    else:
        with st.spinner("Gerando seu roteiro de viagem, aguarde..."):
            research_crew = TripCrew(origin, cities, date_range, interests)
            roteiro = research_crew.run()
        st.subheader("Aqui está o seu roteiro de viagem:")
        st.write(str(roteiro))

        def gerar_pdf(texto):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)
            for linha in str(texto).split('\n'):
                pdf.multi_cell(0, 10, linha)
            return pdf.output(dest="S").encode("latin1")

        pdf_bytes = gerar_pdf(str(roteiro))
        b64 = base64.b64encode(pdf_bytes).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="roteiro_viagem.pdf">Baixar roteiro em PDF</a>'
        st.markdown(href, unsafe_allow_html=True)
