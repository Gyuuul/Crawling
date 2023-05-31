import requests
from bs4 import BeautifulSoup

response= requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%8B%B9%EA%B7%BC%EB%A7%88%EC%BC%93")
html= response.text

soup= BeautifulSoup(html,'html.parser')
links= soup.select('.news_tit')
for link in links:
    title =link.text 
    url =link.attrs['href']

print(title, url)


