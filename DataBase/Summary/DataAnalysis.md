## Data Analysis
1. .csv/.txt는 무쓸모
- 데이터(10TB) -> PC에서 분석 -> 결과 : 불가능
- 데이터(10TB) -> Hadoop(서버급 컴 여러 대로 병렬 전처리)(10MB)
    -> PC에서 분석 -> 결과 : 가능
- Hadoop이 DB 연동 불가, 파일 처리만 가능 -> .csv/.txt 필요
2. Python DB 분석 라이브러리(Numpy, Pandas)는 DB가 AI쪽이 부실하니  
    -> 그 AI 라이브러리가 Numpy, Pandas 사용