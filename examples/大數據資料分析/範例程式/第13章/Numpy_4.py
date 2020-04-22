import numpy as np

#產生1~50之間奇數5x5矩陣
a = np.arange(1, 51, 2).reshape(5, -1)
#產生1~50之間偶數5x5矩陣
b = np.arange(2, 51, 2).reshape(5, -1)

#將矩陣a和矩陣b作垂直堆疊
v_stack = np.concatenate([a, b], axis=0)
#將矩陣a和矩陣b作水平堆疊
h_stack = np.concatenate([a, b], axis=1)

#顯示結果
print('垂直堆疊：\n', v_stack)
print()
print('水平堆疊：\n', h_stack)