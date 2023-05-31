import requests
from bs4 import BeautifulSoup

# 종목코드리스트
codes = [
    '035720',
    '000660',
    '005930',
]
for i in codes:
    url= f"https://finance.naver.com/item/sise.naver?code={i}"
    response= requests.get(url)
    html= response.text
    soup= BeautifulSoup(html, 'html.parser')
    price= soup.select_one("#_nowVal").text
    price = price.replace(',', '')
    print(price)
