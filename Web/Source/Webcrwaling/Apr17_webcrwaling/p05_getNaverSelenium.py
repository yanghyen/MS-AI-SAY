# 웹브라우저 매크로 라이브러리
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
# 이렇게 하면 해당 페이지가 한번 켜지고 꺼짐 
driver.get("https://news.naver.com/")

# driver.execute_script("javaScript 문법") 하면 이런저런 작업들 다 가능 
# 로그인하면 이경로가 다름 주의
news=driver.find_element(By.CSS_SELECTOR,".cc_text_item")
for i in news:
    print(i.text)
    sleep(1)

