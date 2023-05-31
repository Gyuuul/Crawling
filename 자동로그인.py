from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")

# 아이디 입력창
id= driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
#id.send_keys("1234")
pyperclip.copy("1234")
pyautogui.hotkey("ctrl","v")

# 비밀번호 입력창
pw= driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click() # pw를 클릭하겠다.
pyperclip.copy("1234")
pyautogui.hotkey("ctrl","v")

# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, "#log\.login")
login_btn.click()
