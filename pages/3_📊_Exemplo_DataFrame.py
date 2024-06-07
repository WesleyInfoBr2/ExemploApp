import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="Exemplo de DataFrame", page_icon="📊")

st.markdown("# Exemplo de DataFrame")
st.sidebar.header("Exemplo de DataFrame")
st.write(
    """Esta demonstração mostra como usar `st.write` para visualizar 
    DataFrames Pandas. (Dados cortesia do [UN Data Explorer]
    (http://data.un.org/Explorer.aspx).)"""
)


@st.cache_data
def get_UN_data():
    AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")


try:
    df = get_UN_data()
    countries = st.multiselect(
        "Selecione os países", list(df.index), ["China", "United States of America","Brazil"]
    )
    if not countries:
        st.error("Selecione pelo menos um país.")
    else:
        data = df.loc[countries]
        data /= 1000000.0
        st.write("### Produção Agrícola Bruta ($B)", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
        )
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                color="Region:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(
        """
        **Esta demonstração requer acesso à Internet.**
        Erro de conexão: %s
    """
        % e.reason
    )