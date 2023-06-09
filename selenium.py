from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManagerhttps://github.com/Gyuuul/Crawling/tree/main

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.naver.com")
