import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Exemplo de Gráfico", page_icon="📈")

st.markdown("# Exemplo de Gráfico")
st.sidebar.header("Exemplo de Gráfico")
st.write(
    """Esta demonstração ilustra uma combinação de plotagem 
    e animação com Streamlit. Estamos gerando um monte de números 
    aleatórios em um loop por cerca de 5 segundos. Aproveite!"""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Completo" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Os widgets Streamlit executam automaticamente o script de 
# cima para baixo. Como este botão não está conectado a nenhuma 
# outra lógica, ele apenas causa uma simples reexecução.
st.button("Re-run")