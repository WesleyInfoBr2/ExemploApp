import streamlit as st

st.set_page_config(
    page_title="Bem-vindo",
    page_icon="👋",
)

st.write("# Bem-vindo ao Streamlit! 👋")

st.sidebar.success("Selecione uma das demonstrações.")

st.markdown(
    """
    O Streamlit é um de aplicativo de código aberto criada 
    especificamente para projetos de aprendizado de máquina e 
    ciência de dados. 
    **👈 Selecione uma demonstração na barra lateral** para 
    ver alguns exemplos do que o Streamlit pode fazer!
    
    ### Quer aprender mais?
    - Confira [streamlit.io](https://streamlit.io)
    - Acesse a [documentação](https://docs.streamlit.io)
    - Faça perguntas nos [fóruns da comunidade](https://discuss.streamlit.io)
    ### Veja demonstrações mais complexas
    - Use uma rede neural para [analisar o conjunto de dados de imagens de 
    carros autônomos da Udacity](https://github.com/streamlit/demo-self-driving)
    - Explore um [conjunto de dados de compartilhamento de viagens na cidade de 
    Nova York](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)