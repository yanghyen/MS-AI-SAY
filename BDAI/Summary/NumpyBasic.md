# NumPy
- NumPy: list 기능 개선판, Python 빅데이터 분석 라이브러리
### broadcasting: 모양이 다르면 차원수 높은 쪽에서 맞춰서 계산
### masking: True인 index만 
```print(name[name[50 < eng < 70]])```
- 안되는 이유: &&가 아니라 &여야 해서. 즉 조건식 중간에 skip되는 형태면 안되고 끝까지 가는 and/or 말고 &/|로 써야 함