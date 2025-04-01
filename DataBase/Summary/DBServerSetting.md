## 서버에 DB 설치
### 서버
1. Oracle 18c XE 서버 설치
- OracleXE184_Win64 압축 해제 후 setup.exe 실행해서 설치
2. DB파일 저장될 폴더 확보
- C:/ms/odb
3. 통신 정보 확인
- IP 주소
```ipconfig```로 IPv4체크  
- IP주소 : 195.168.9.126
- 포트번호 : 1521
- DB 이름 : xe
- 방화벽 off
5. 로컬 관리자 계정으로 접속
```sqlplus / as sysdba```
- sqlplus : OracleDB 접속할 때 쓰는 프로그램명
- / : OS의 계정 써서
6. 11gR2 -> 18c 문법이 바뀌어서 꼐정 만들 때 C## 넣어야 함. 이전 문법으로 되돌리기  
```alter session set "_ORACLE_SCRIPT"=true;```
7. 원격접속 가능한 관리자 계정 만들기(서버 사용자들과 공유)
    - 계정 만들기  
    ```create user [id] identified by [pw];```
    - 권한 부여  
    ```grant connect,resource,dba to [id];```


### 로컬
4. 서버와 통신 여부 확인  
```ping <IP주소>```
8. OracleDB 접속 
- 구글에 ```instatnclient``` 검색
- Basic Package  
  SQL*Plus Package  
  JDBC Suplement Package(JavaDBConnector : Python도 사용)  
  다운로드 후 한 파일로 압축 해제
    - 이때 압축해제가 한번에 안되면 각각 압축 해제 후 ```instantclient_23_7``` 내 파일만 합치기
    - META-INF 필요없음
9. 관리자 계정으로 접속  
- ../instantclient/ cmd에서  
```sqlplus id/pw@<IP주소>:<포트번호>/DB이름```
    
10. 계정 만들기  
10.0 이전 문법으로  
```alter session set "_ORACLE_SCRIPT"=true;```  
10-1. 계정 만들기  
```create user id identified by pw;```  
10-2. role(권한 세트) 부여  
```grant connect, resource to id;```  
10.3 tablespace 만들기  
```create tablespace <table name> datafile '<path>' size <size>;```  
```create tablespace yangTs datafile 'C:/ms/odb/yangTS.dbf' size 500m;```  
10.4 계정에게 tablespace 부여  
```alter user id default tablespace <TS명> quota unlimited on <TS명>;```  
```alter user yanghyen default tablespace yangTS quota unlimited on yangTS;```  
**여기까진 관리자 계정으로 로그인된 상태**니 닫고
11. 본인 계정으로 접속  
```sqlplus id/pw@<IP주소>:<포트번호>/DB이름```  
```sqlplus id/pw@<IP주소>:<포트번호>/DB이름```

### 참고
- Python은 SQL인 OracleDB를 제어하는 컴퓨터 언어