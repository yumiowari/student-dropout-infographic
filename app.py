import streamlit as st
from plots import dropout_rate_per_year, cumulative_dropout_rate, dropout_rate_per_age, dropout_rate_per_env, dropout_rate_per_financing

# Configuração da página
st.set_page_config(
    page_title='Infográfico Explanatório',
    #page_icon='',
    layout='centered' # 'centered' ou 'wide'
)

# Título e cabeçalho
st.title('Censo da Educação Superior 2024')

# Corrige a formatação para a função de impressão
st.markdown("""
    <style>
    @media print {
        /* 1. Reduz o gap entre os elementos */
        div[data-testid="stVerticalBlock"]{
            gap: 1rem !important;
        }

        /* Evite quebra de página dentro dos blocos principais */
        div[data-testid="stVerticalBlock"] > div{
            page-break-inside: avoid;
        }
        
        /* Diminui a escala dos gráficos (1 -> 0.8) e elimina o espaço extra gerado pela redução */
        div[data-testid="stImage"]{
            transform: scale(0.8);
            transform-origin: top center;
            margin-top: -1rem !important;
            margin-bottom: -2rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Conteúdo principal
with st.container():
    st.write('Em uma década, a evasão no sistema de ensino superior brasileiro deu um salto preocupante: passou de 11,8% em 2013-2014 para 17,5% em 2023-2024, acumulando um aumento de 48,3% no período.')
    st.pyplot(dropout_rate_per_year())

with st.container():
    st.write(
        'A trajetória dos alunos revela uma perda expressiva a longo prazo: mais da metade (54%) dos ingressantes de 2015 abandonaram a graduação em até cinco anos de estudo.'
    )
    st.pyplot(cumulative_dropout_rate())

with st.container():
    st.write(
        'A probabilidade de desistência cresce significativamente de acordo com a idade: em 2023-2024, estudantes com 50 anos ou mais atingiram 23,4% de evasão.'
    )
    st.pyplot(dropout_rate_per_age())

with st.container():
    st.write(
        'A distância física é outro fator crítico: a modalidade EaD registrou 24,1% de evasão em 2023-2024, mais que o dobro em comparação com o ensino presencial (9,5%).'
    )
    st.pyplot(dropout_rate_per_env())

with st.container():
    st.write(
        'Quanto ao apoio financeiro em 2023-2024, estudantes com financiamentos não reembolsáveis apresentaram taxa de evasão mais elevada (19,7%) do que aqueles com apoio reembolsável (15,5%).'
    )
    st.pyplot(dropout_rate_per_financing())

with st.container():
    # Call-to-action
    st.write(
        'A evasão no ensino superior é um desafio complexo, mas a análise dos dados viabiliza a identificação de grupos de risco, permitindo que políticas de permanência sejam direcionadas com maior precisão.'
    )