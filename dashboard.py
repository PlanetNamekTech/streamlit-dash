from urllib import response
import streamlit as st
import requests
from decouple import config

API_KEY = config('POLYGON_API_KEY')
symbol = st.sidebar.text_input("Symbol", value="MSFT").upper()

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership', 'Technicals'))

st.title(screen)
if screen == 'Overview':
  url = f"https://api.polygon.io/v3/reference/tickers/{symbol}?apiKey={API_KEY}"
  r = requests.get(url)
  response_json = r.json()

  st.title(response_json['results']['ticker'])
  st.image(f"https://companiesmarketcap.com/img/company-logos/64/{symbol}.webp")
  st.write(response_json['results']['description'])

if screen == 'Fundamentals':
  pass