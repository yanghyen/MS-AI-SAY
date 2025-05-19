import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pdfplumber
import re
import requests

class Data:
    def getFluRatioPdfUrl():
        service = Service('C:/Yang/workspace/Project/MaskOnOff/Data/parsingData/chromedriver.exe')
        driver = webdriver.Chrome(service=service)

        PHWRUrl = "https://www.phwr.org/journal/archives_Supple.html"
        driver.get(PHWRUrl)

        fluRatioPdfPageXPath = "/html/body/div[2]/div[8]/div[1]/div[2]/table/tbody/tr[2]/td/a"
        fluRatioPdfUrlXPath = "/html/body/div[2]/div[8]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td/embed"

        try:
            link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, fluRatioPdfPageXPath))
            )
            link.click()

            embedElement = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, fluRatioPdfUrlXPath))
            )

            fluRatioPdfUrl = embedElement.get_attribute("src")

            return fluRatioPdfUrl

        except Exception as e:
            print(f"오류 발생 : {e}")
        finally:
            driver.quit()

    logging.getLogger("pdfminer").setLevel(logging.ERROR)
    def getFluRatio(fluRatioPdfUrl):
        pdfUrl = fluRatioPdfUrl

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        savePath = r'C:/Yang/workspace/Project/MaskOnOff/Data/pdfFile/downloaded_file.pdf'

        try:
            response = requests.get(pdfUrl, headers=headers)
            response.raise_for_status()

            with open(savePath, "wb") as f:
                f.write(response.content)
            print("pdf 파일 다운로드 완료!")
        except Exception as e:
            print(f'요청 실패 : {e}')
            exit(1)

        with pdfplumber.open(savePath) as pdf:
            allText = ""
            for page in pdf.pages:
                allText += page.extract_text()

        match = re.search(r'의사환자분율\(ILI\):\s*(\d+\.\d+)', allText)

        if match:
            fluRatio = match.group(1)
            return fluRatio
        else:
            print("의사환자분율(ILI)을 찾을 수 없습니다.")
