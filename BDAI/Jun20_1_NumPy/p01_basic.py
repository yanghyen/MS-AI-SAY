score = [[100, 90, 80], [50, 60, 100]]
print(score)
print(type(score))
print(score[0])
print(score[0][1])
score[1]
print(score)
print("-------------------")

import numpy as np
score2 = np.array(score)
print(score2)
print(type(score2))
print(score2[0][1])     # 기존 list스타일
print(score2[0, 1])     # NumPy 스타일
score2[1, 2] = 2
print(score2)
print(score2.shape)
print(score2.dtype)
print(len(score2))
print(score2.size)