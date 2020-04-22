import numpy as np

a = np.array([30, 65, 21, 90, 27, \
           43, 67, 60, 87, 72])

b = np.array([52, 91, 38, 22, 27, 60]) 

c = np.arange(5, 96, 10)

#集合a和b交集
intersection = np.intersect1d(a, b)

#集合a和c差集
difference = np.setdiff1d(a, c)

#集合a和b聯集
union = np.union1d(a, b)

print("交集結果：", intersection)
print("差集結果：", difference)
print("聯集結果：", union)