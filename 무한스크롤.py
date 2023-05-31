from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

import time

from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 자동 업데이트

from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동

driver.get("https://shopping.naver.com/home")

# 페이지 이동 전에 검색창 실행 방
time.sleep(2)

# 검색창 클릭
search= driver.find_element(By.CSS_SELECTOR, "._searchInput_search_text_3CUDs")
search.click()

# 검색어 입력
search.send_keys('아이폰 14')
search.send_keys(Keys.ENTER)

#스크롤 전 높이
before_h = driver.execute_script("return window.scrollY")

# 무한스크롤 = 반복문, while 안에 있는 걸 무한 반복
while True:
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    # 스크롤을 할 때 정보가 로딩 걸리지 않도록 시간을 둘 것
    time.sleep(1)

    # 스크롤 후 높이
    after_h = driver.execute_script("return window.scrollY")

    if after_h==before_h:
        break

    before_h=after_h

items = driver.find_elements(By.CSS_SELECTOR, ".basicList_info_area__TWvzp") 

for item in items:
    name = item.find_element(By.CSS_SELECTOR,".basicList_title__VfX3c").text
    price = item.find_element(By.CSS_SELECTOR,".price_num__S2p_v").text
    link = item.find_element(By.CSS_SELECTOR,".basicList_title__VfX3c> a").get_attribute('href')
    print(name, price, link)
