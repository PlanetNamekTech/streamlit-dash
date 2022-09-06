import requests

class PolygonStock:
  def __init__(self, token, symbol):
    self.BASE_URL = "https://api.polygon.io/v3/reference"
    self.token = token
    self.symbol = symbol

  def get_company_info(self):
    url = f"{self.BASE_URL}/tickers/{self.symbol}?apiKey={self.token}"
    r = requests.get(url)
    return r.json()

  def get_stats(self):
    url = f"{self.BASE_URL}/tickers/{self.symbol}?apiKey={self.token}"
    r = requests.get(url)
    return r.json()