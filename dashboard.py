import streamlit as st
import requests
from decouple import config

API_KEY = config('POLYGON_API_KEY')
symbol = st.sidebar.text_input("Symbol", value="MSFT")

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership', 'Technicals'))

st.title(screen)
if screen == 'Overview':
  url = f"https://api.polygon.io/v3/reference/tickers/AAPL?apiKey={API_KEY}"
  r = requests.get(url)
  st.write(r.json())
if screen == 'Fundamentals':
  pass