import streamlit as st
from utils.load_styles import load_styles
from utils.var import REGIONS
from api.riot_api_handler import get_summoner_puuid, get_summoner_matchs
from model.instance import MODEL
from utils.preprocessing import format_data

st.set_page_config(
    page_title="LoL Stats",
    page_icon="https://i.imgur.com/uSOsaIZ.jpeg",
    layout="centered",
)
load_styles()


c1, c2 = st.columns((4, 1))
nick_name = c1.text_input("Seu nome de invocador", placeholder="shadyzled006#faker")
region = c2.selectbox("Selecione sua região", options=REGIONS.keys())

button = st.button("Buscar")


if nick_name and button:
    # try:
        nick, tag = nick_name.split("#")
        puuid = get_summoner_puuid(nick, tag, REGIONS.get(region), st.error)
        matchs = get_summoner_matchs(puuid, REGIONS.get(region))

        format_data(matchs)

        pred = MODEL.predict(matchs)
        st.dataframe(matchs['win'])
        st.dataframe(pred)
    # except ValueError:
    #     st.error("Nome de invocador inválido")
