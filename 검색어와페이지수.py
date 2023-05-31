import requests
from bs4 import BeautifulSoup
import pyautogui

keyword= pyautogui.prompt("검색어를 입력하세요.")
lastpage= pyautogui.prompt("마지막 페이지 번호를 입력하세요.")
pagenum=1
for i in range(1,int(lastpage)*10,10):
    print(f"============={pagenum}페이지입니다=============")
    response= requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}" )
    html= response.text
    soup= BeautifulSoup(html,'html.parser')
    links= soup.select('.news_tit')
    for link in links:
        title =link.text
        url =link.attrs['href']
        print(title, url)
    pagenum= pagenum+1

