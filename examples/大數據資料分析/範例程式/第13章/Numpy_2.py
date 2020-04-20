import numpy as np

matrix1 = np.random.randint(1, 51, 12).reshape(3, 4)
matrix2 = np.random.randint(1, 51, 20).reshape(4, 5)

#顯示matrix1
print('matrix1: \n%s' % matrix1)

#顯示matrix2
print('\nmatrix2: \n%s' % matrix2)

#顯示matrix1每一列的最大值
print('\nmatrix1每一列的最大值：%s' % np.amax(matrix1, axis=1))

#輸出matrix1第2列小於30的個數
print("\nmatrix1第2列小於30的個數：%d" % np.sum(matrix1[2, :] < 30))

#顯示matrix2每一欄的最大值
print('\nmatrix2每一欄的最大值：%s' % np.amax(matrix2, axis=0))

#輸出matrix2第2欄小於30的個數
print("\nmatrix2第2欄小於30的個數：%d" % np.sum(matrix2[:, 2] < 30))

#輸出matrix1第一列和matrix2第一列的聯集結果
print('\nmatrix1第一列和matrix2第一列的聯集結果：%s' % np.union1d(matrix1
[0,:], matrix2[0,:]))

#輸出matrix1*matrix2的結果
print('\nmatrix1 * matrix2: \n%s' % np.dot(matrix1, matrix2))