import pdfplumber
import re
import requests

# PDF 파일의 URL
pdf_url = 'https://pdf.medrang.co.kr/PHWR/Supple/2025/018/PHWR_Supple_18-13.pdf'

# 요청 헤더에 User-Agent 추가
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
save_path = r'C:/Yang/workspace/Project/MaskOnOff/Data/pdfFile/downloaded_file.pdf'
# PDF 파일 다운로드
try:
    response = requests.get(pdf_url, headers=headers)
    response.raise_for_status()  # HTTP 상태 코드가 200이 아닌 경우 예외 발생

    # PDF 파일이 제대로 다운로드 되었는지 확인
    with open(save_path, "wb") as f:
        f.write(response.content)
    print("PDF 파일 다운로드 완료!")

except requests.exceptions.RequestException as e:
    print(f"요청 실패: {e}")
    exit(1)

# PDF 파일 열기
with pdfplumber.open(save_path) as pdf:
    # 모든 페이지에서 텍스트 추출
    all_text = ""
    for page in pdf.pages:
        all_text += page.extract_text()

# 추출된 텍스트 출력 (확인용)
# print(all_text)

# 정규표현식을 사용해 의사환자분율(ILI) 값 추출
# 예: "외래환자 1,000명당 의사환자분율(ILI): 13.2명(=1.3%)"
match = re.search(r'의사환자분율\(ILI\):\s*(\d+\.\d+)', all_text)

if match:
    doctor_patient_rate = match.group(1)
    print(f"의사환자분율(ILI): {doctor_patient_rate}명")
else:
    print("의사환자분율(ILI)을 찾을 수 없습니다.")
