from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
# 확인 필요!!!
# 데이터 검증 및 파일 기록에 관련된 별도의 유틸리티 클래스를 추가합니다.
class CSVUtils:
    @staticmethod
    def safe_str(value, default=''):
        """None 또는 빈 값이 있을 경우 기본값으로 대체"""
        return value if value else default

    @staticmethod
    def write_to_csv(f, data):
        """CSV 형식으로 데이터를 파일에 저장"""
        f.write(",".join(str(item) for item in data) + "\n")

# DustData 클래스: 미세먼지 데이터 구조만 담당
class DustData:
    def __init__(self, msrdt, msr_region, msr_ste, pm10, pm25, index_nm):
        self.msrdt = msrdt
        self.msr_region = msr_region
        self.msr_ste = msr_ste
        self.pm10 = pm10
        self.pm25 = pm25
        self.index_nm = index_nm

    def parse_date(self):
        """날짜를 '2025,03,26,17' 형식으로 반환"""
        return ",".join([self.msrdt[0:4], self.msrdt[4:6], self.msrdt[6:8], self.msrdt[8:10]])

    def to_csv_row(self):
        """DustData 객체를 CSV 형식으로 변환"""
        return [
            self.parse_date(),
            CSVUtils.safe_str(self.msr_region),
            CSVUtils.safe_str(self.msr_ste),
            CSVUtils.safe_str(self.pm10),
            CSVUtils.safe_str(self.pm25),
            CSVUtils.safe_str(self.index_nm)
        ]

# DustCollector 클래스: 미세먼지 데이터를 수집하고 파일에 저장
class DustCollector:
    def __init__(self, api_url, csv_file_path):
        self.api_url = api_url
        self.csv_file_path = csv_file_path

    def fetch_data(self):
        """서울시 미세먼지 데이터를 API로부터 받아오는 함수"""
        hc = HTTPConnection(self.api_url, 8088)
        hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")
        resBody = hc.getresponse().read()
        hc.close()
        return resBody

    def parse_data(self, resBody):
        """XML 데이터를 파싱하여 DustData 객체 리스트로 반환"""
        dustData = fromstring(resBody)
        dusts = dustData.iter("row")
        dust_objects = []
        for d in dusts:
            msrdt = d.find("MSRDT").text
            msr_region = d.find("MSRRGN_NM").text
            msr_ste = d.find("MSRSTE_NM").text
            pm10 = d.find("PM10").text
            pm25 = d.find("PM25").text
            index_nm = d.find("IDEX_NM").text
            dust_object = DustData(msrdt, msr_region, msr_ste, pm10, pm25, index_nm)
            dust_objects.append(dust_object)
        return dust_objects

    def save_to_csv(self, dust_objects):
        """DustData 객체들을 CSV 파일에 저장하는 함수"""
        with open(self.csv_file_path, "a", encoding="utf-8") as f:
            for dust in dust_objects:
                row = dust.to_csv_row()
                CSVUtils.write_to_csv(f, row)

    def collect_and_save(self):
        """전체 프로세스를 한 번에 실행"""
        resBody = self.fetch_data()
        dust_objects = self.parse_data(resBody)
        self.save_to_csv(dust_objects)

# 프로그램 실행
if __name__ == "__main__":
    collector = DustCollector("openapi.seoul.go.kr", "C:/Yang/seoulDust.csv")
    collector.collect_and_save()
