## 迴歸
### 邏輯迴歸
* 範例
<pre>
假設我們的邏輯回歸模型具有學習了下列偏差和權重的三個特徵：
    •	b = 1
    •	w1 = 2
    •	w2 = -1
    •	w3 = 5
進一步假設給定樣本具有以下特徵值：
    •	x1 = 0
    •	x2 = 10
    •	x3 = 2
因此，對數幾率：
b+w1x1+w2x2+w3x3
將是：
  (1) + (2)(0) + (-1)(10) + (5)(2) = 1
因此，此特定樣本的邏輯回歸預測值將是 0.731：
y′=1/1+e−(1)=0.731
 
</pre>
![Logistic regression](images/logistic.png)
#### 參考連結
* [机器学习](https://developers.google.com/machine-learning/crash-course/logistic-regression/calculating-a-probability?hl=zh-cn)
* [線性回歸](http://www1.pu.edu.tw/~hdchen/handout_bank/stat/94_4_stat_handout_08.pdf)
