# Exception Handling
- error : compile 불가능
    - 프로그램 소스가 이상해서 기계어로 번역 불가능
    - 최종 실행 파일이 나오지 않아 실행 불가
- warning : 지저분한 소스
    - 불필요한 작업 or 쓰고 정리 안 한 것
    - 실행은 가능
## exception 
- 프로그램 완성됐고, 실행 잘됨
- But, 실행할 때 외부적 요인에 의해 정상 실행 불가
- 개발자는 대비해둘 필요가 있음
- Python 관점 error, warning, exception
    - interpreter 언어 : 한국어 -번역(coding)-> 프로그램소스    : 개발자
    - 프로그램 소스 -실행->                                    : 사용자
                      소스 한줄 기계어로 번역해서 실행하고      : 언어가 알아서
                      그 다음 줄 기계어로 번역해서 실행하고
    => error/exception 경계 애매 => error 잡기 힘듦
- 예시 : 수학에서 나누기 0은 없음 

## exception handling
- 문제 생길만한 위험을 파악해서 대비책 마련해두자
```py
try:
    d = x / y
    print("----------")
    print(d)

    e = [43, 23, 23]
    print(e[y])
except ZeroDivisionError:
    print("나누기 0은 없슴")
except IndexError:
    print("리스트 범위 넘음")
```
## OOP
- polymorphism(다형성)
- 다형성 지원하는 언어는 상위타입(Animal)변수에 하위타입(개)데이터 가능
    - Dog d1 = 개;
      Cat c1 = 고양이;
      둘은 다 에러
    - Animal a = 개;
      는 에러 아님요
- Python 모든 변수의 자료형 : object
    = 다형성 지원 
    - 상위타입(object)변수에 하위타입(str, int, ...)데이터 써왔음
```py
try:
    d = x / y
    print("----------")
    print(d)

    e = [43, 23, 23]
    print(e[y])
except Exception as e:
    print("쨌든 잘못됨")
    print(e)    # e에 error 사유 담김

finally:
    pirnt("문제 발생 여부 상관없이 쨌든 실행")
```
    - 다형성을 이용해서 모든 에러 잡기
    - Exception으로부터 상속받는 IndexError
- 왜 굳이 finally 씀?
    - 문제가 있었든 없었든 무조건 실행 + **return보다 먼저 실행**
- 예시
    ```py
    data = input().split(',')
    print("---------------")

    sum = 0
    cnt = 0
    for v in data:
        try:
            v = int(v)
            sum += v
            cnt += 1
        except:
            pass

    print("합계 : %d" % sum)
    print("평균 : %.1f" %(sum / cnt))
    ```
    - 인풋에 글자 포함돼있으면 무시하고 정수형 객체 생성하고 합계와 평균 구함