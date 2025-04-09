from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome WebDriver 설정
service = Service('C:/Yang/workspace/Project/MaskOnOff/Data/parsingData/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# 1. 첫 번째 페이지로 이동: PDF를 열 수 있는 링크 클릭
driver.get("https://www.phwr.org/journal/archives_Supple.html")  # 기본 URL로 웹 페이지를 엽니다.

try:
    # 첫 번째 XPath로 PDF 페이지로 이동
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[8]/div[1]/div[2]/table/tbody/tr[2]/td/a"))
    )
    link.click()

    # 2. PDF URL 추출: 두 번째 XPath에서 embed 태그의 src 속성값 추출
    embed_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[8]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td/embed"))
    )
    
    # embed 태그에서 src 속성 추출 (PDF URL)
    relative_pdf_url = embed_element.get_attribute("src")
    
    # 상대 주소 그대로 사용
    print("PDF URL (상대 주소):", relative_pdf_url)

except Exception as e:
    print(f"오류 발생: {e}")

finally:
    driver.quit()
