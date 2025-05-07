from crewai import Task
from textwrap import dedent


class TravelTasks:
    def __tip_section(self):
        return "Se você fizer o seu MELHOR TRABALHO, vou te dar uma comissão de R$ 10.000!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
            **Tarefa**: Desenvolver um roteiro de viagem de 7 dias
            **Descrição**: Expanda o guia da cidade em um roteiro completo de 7 dias com planos detalhados por dia, incluindo previsões do tempo, lugares para comer, sugestões de bagagem e uma divisão do orçamento. Você DEVE sugerir lugares reais para visitar, hotéis reais para se hospedar e restaurantes reais para ir. Este roteiro deve cobrir todos os aspectos da viagem, desde a chegada até a partida, integrando as informações do guia da cidade com a logística prática da viagem.

            **Parâmetros**:
            - Cidade: {city}
            - Data da viagem: {travel_dates}
            - Interesses do viajante: {interests}

            **Nota**: {self.__tip_section()}
            IMPORTANTE: Responda sempre em português do Brasil.
        """
            ),
            agent=agent,
            expected_output=dedent(
                """
                Um roteiro completo de 7 dias, incluindo:
                - Detalhamento das atividades por dia
                - Hotéis, restaurantes e atrações recomendados
                - Orçamento estimado e previsão do tempo
                """
            ),
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
                    **Tarefa**: Identificar a melhor cidade para a viagem
                    **Descrição**: Analise e selecione a melhor cidade para a viagem com base em critérios como padrões climáticos, eventos sazonais e custos de viagem. Esta tarefa envolve comparar várias cidades, considerando fatores como condições climáticas atuais, eventos culturais ou sazonais e despesas gerais de viagem. Sua resposta final deve ser um relatório detalhado sobre a cidade escolhida, incluindo custos reais de voos, previsão do tempo e atrações.

                    **Parâmetros**:
                    - Origem: {origin}
                    - Cidades: {cities}
                    - Interesses: {interests}
                    - Data da viagem: {travel_dates}

                    **Nota**: {self.__tip_section()}
                    IMPORTANTE: Responda sempre em português do Brasil.
        """
            ),
            agent=agent,
            expected_output=dedent(
                """
                - A melhor cidade para a viagem com base nos parâmetros fornecidos
                - Justificativa incluindo custo, clima e eventos
                - Preços de voos e despesas esperadas
                """
            ),
        )

    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                    **Tarefa**: Reunir informações detalhadas sobre a cidade
                    **Descrição**: Compile um guia aprofundado para a cidade selecionada, reunindo informações sobre principais atrações, costumes locais, eventos especiais e recomendações de atividades diárias. Este guia deve fornecer uma visão completa do que a cidade tem a oferecer, incluindo pontos turísticos, locais culturais, pontos de referência imperdíveis, previsões do tempo e custos gerais.

                    **Parâmetros**:
                    - Cidade: {city}
                    - Interesses: {interests}
                    - Data da viagem: {travel_dates}

                    **Nota**: {self.__tip_section()}
                    IMPORTANTE: Responda sempre em português do Brasil.
        """
            ),
            agent=agent,
            expected_output=dedent(
                """
                - Um guia detalhado da cidade incluindo:
                - Principais atrações, costumes locais e eventos especiais
                - Previsão do tempo e custos estimados
                """
            ),
        )
