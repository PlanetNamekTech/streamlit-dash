from urllib import response
import streamlit as st
import requests
from requests.structures import CaseInsensitiveDict
from decouple import config

API_KEY = config('POLYGON_API_KEY')
symbol = st.sidebar.text_input("Symbol", value="MSFT")

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership', 'Technicals'))

print(API_KEY)

st.title(screen)
if screen == 'Overview':
  url = f"https://api.polygon.io/v3/reference/tickers/AAPL?apiKey={API_KEY}"
  headers = CaseInsensitiveDict()
  headers["Authorization"] = "Bearer YPijiFRXWt61xNTCyGZOftwxq02SgZUG"
  r = requests.get(url, headers=headers)
  response_json = r.json()
  st.image(response_json['results']['branding']['logo_url'])
if screen == 'Fundamentals':
  pass