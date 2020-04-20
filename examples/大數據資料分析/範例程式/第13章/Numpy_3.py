import numpy as np
#建立一個1到200之間偶數的10x10矩陣
a = np.arange(2, 201, 2).reshape(10, 10)
#建立一個1到200之間奇數的10x10矩陣
b = np.arange(1, 200, 2).reshape(10, 10)
print('交換前：')
print('a:')
print(a)
print('b:')
print(b)

print()

#將兩個矩陣的偶數列作交換
a[range(1, 10, 2)], b[range(1, 10, 2)] = b[range(1, 10, 2)], a[range(1, 10, 2)]
print('交換後：')
print('a:')
print(a)
print('b:')
print(b)