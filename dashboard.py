from urllib import response
import streamlit as st
import yfinance as yf
from decouple import config
from polygon import PolygonStock
from helpers import format_number

API_KEY = config('POLYGON_API_KEY')
symbol = st.sidebar.text_input("Symbol", value="MSFT").upper()
stock = PolygonStock(API_KEY, symbol)
yfsymbol = yf.Ticker(symbol)

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'Dividends', 'Ownership', 'Technicals'))

st.subheader(screen)
if screen == 'Overview':
  # Put into a class for repetition
  company_info = stock.get_company_info()
  # Partition the information into columns with a Streamlit feature
  col1, col2 = st.columns([1,4])
  with col1:
    st.image(f"https://companiesmarketcap.com/img/company-logos/64/{symbol}.webp")
  with col2:
    st.subheader(company_info['results']['name'])
    st.write(company_info['results']['description'])
    st.write("Market Cap: ",format_number(company_info['results']['market_cap']))
    st.write("Headquartered in ", company_info['results']['address']['city'].capitalize(), ",", company_info['results']['address']['state'])
    st.write("Company Site: ", company_info['results']['homepage_url'])
    

if screen == 'Fundamentals':
  pass

if screen == 'Dividends':
  st.write(yfsymbol.dividends)