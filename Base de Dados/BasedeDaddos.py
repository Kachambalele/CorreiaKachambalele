import streamlit as st
import panda as pd
import numpy as np

st.title("Base de Dados")

st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox("League", ['England', 'Germany', 'Italy', 'Belgiun', 'Netherland', 'Spain', 'France', 'Portugal', 'Turkie', 'Scotiland'])
st.sidebar.header("Season")
selected_league = st.sidebar.selectbox("League", ['England', 'Germany', 'Italy', 'Belgiun', 'Netherland', 'Spain', 'France', 'Portugal', 'Turkie', 'Scotiland'])
st.sidebar.header("Season")
selected_league = st.sidebar.selectbox("League", ['2021/2022', '2022/2023', '2023/2024', '2024/205'])
def load_data(league, season):
  url = "https://www.football-data.co.uk/mmz4281/"season"/"league".csv"
  data = pd.read_csv(url)
  return data

df = load_data(selected_league, selected_season)
  
