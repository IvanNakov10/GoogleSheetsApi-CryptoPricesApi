from openpyxl import Workbook
import requests

def getPriceOfCrypto():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  par={
     'symbol' : 'BTC, ETH, GALA' ,
     'convert' : 'USD'
  }
  headers = {
     'Accepts': 'application/json',
     'X-CMC_PRO_API_KEY': '634562be-a173-41d3-8c5d-e4229f52baea'
  }

  response = requests.get(url, headers=headers, params=par)

  data = response.json()

  btc = round(data['data']['BTC']['quote']['USD']['price'], 2)
  eth = round(data['data']['ETH']['quote']['USD']['price'], 2)
  gal = round(data['data']['GALA']['quote']['USD']['price'], 5)

  btcpriceIvan = btc*0.001 
  galaamount = gal*630.8
  ethamount = eth*0.05227
  hole_amount = round(btcpriceIvan+galaamount+ethamount, 2)









wb = Workbook()
ws = wb.active
ws.title = 'chart'

rows = [
    ('Month', 'Apple Sales', 'Banana Sales'),
    ('Jan', 100, 200),
    ('Feb', 200, 300),
    ('Mar', 300, 400),
    ('Apr', 50, 20),
    ('May', 500, 600),
    ('Jun', 100, 200),
]

for row in rows:
    ws.append(row)

wb.save('chart_eg.xlsx')