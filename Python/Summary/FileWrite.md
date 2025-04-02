## 파일 저장
- 데이터 -> 임시저장 : 변수 형태로 RAM에 저장
데이터 -> 영구저장 : 파일 형태로 SSD/HDD에 저장
- 확장자 : MS Window에 있는 허상. 파일의 정체 짐작하게 해주는 존재
	- .txt : 메모자엥서 열면 잘 열릴 것 같은 파일
  	- .xls : 엑셀에서 열면 잘될 파일
- 경로
	- Windows : 대소문자 구별X, \
	- Linux : 대소문자 구별, /
- 파일 열기
	- 파일은 만들어주지만, 드라이브/폴더는 안 만들어줌
	- open("경로", "a", encoding="utf-8")
	- r : read
	- w : write(기존 내용 지우고)
	- a : append(기존 내용 뒤에 추가)
- 파일 읽기
    1. 전체를 다 읽어서 str로
    ```py
    data = f.read()
    ```
    2. 다음 한 줄 읽어서 str로
    ```py
    data = f.readline()
    ```
    3. 전체를 다 읽어서, 엔터키 기준으로 나눠서 list로
    - 데이터에 \n 남아있음
    ```py
    data = f.readlines()
    for line in data:
        line = line.replace("\n", "")
        print(line)
    ```

- WORA(Write Once, Run Anywhere)
	- 시스템 : Win, Linux, Unix, Mac, Android, iOS, ...
	- 시스템 당 프로그램 개별 생성해야 함
	- WORA는 개별 생성 안 해도 되는 장점이 있다고 주장
	- 이게 무슨 의미?
	: 
- utf-8 왜 주력?
	- Linux가 주로 써서 