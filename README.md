<pre>
%tensorflow_version 1.x
</pre>
# DataScience_1082
Data Science class for CSU CSIE
## 大數據及雲端服務應用
### Date
* 3/12、3/19、3/26、4/9、4/16、4/23
### [課堂練習](inclass.md)
### 課綱
* 數據取得與存檔
    * 以PowerBI 執行資料取得與前處理：CSV、Excel、web、pdf [[ppt]](https://github.com/jumbokh/DataScience_1082/blob/master/Power%20BI.pptx)
    * Python 數據操作：尋找數據、數據清洗、規一化、標準化
    * 網頁爬取
    * 社群網路分析 [[DOC]](https://github.com/jumbokh/DataScience_1082/blob/master/data/FB-Likes-doc.pdf) [[PPT]](https://github.com/jumbokh/DataScience_1082/blob/master/data/fb-likes.pdf) [[範例]](https://github.com/jumbokh/DataScience_1082/blob/master/data/example/C13/C13E01%20-%20Solution.pbit) [[範例: 朋友按讚統計]](https://github.com/jumbokh/DataScience_1082/blob/master/data/ex-fb-friend-like.pbix)
    * [政府公開資料](https://data.gov.tw/) [[pdf]](https://github.com/jumbokh/DataScience_1082/blob/master/data/opendata.pdf)
        * [景點--觀光資訊資料庫](https://github.com/jumbokh/DataScience_1082/blob/master/data/108itaiwanhotspots.csv) [pbix](https://github.com/jumbokh/DataScience_1082/blob/master/data/tw-travel.pbix)
* 數據分析
    * [大數據](https://github.com/jumbokh/intro-computers/blob/master/BigData.md)
    * [機器學習](https://github.com/jumbokh/intro-computers/blob/master/ML_ClassD1.pdf)
    * [聚類範例一](https://github.com/jumbokh/intro-computers/blob/master/refers/%E8%81%9A%E9%A1%9E%E7%AF%84%E4%BE%8B6.pdf) [[Notebook]](https://nbviewer.jupyter.org/github/jumbokh/DataScience_1082/blob/master/src/immp_sompy_simple.ipynb)
    * [聚類範例二](https://nbviewer.jupyter.org/github/jumbokh/DataScience_1082/blob/master/src/immp_som.ipynb)
        * ![圖一](https://github.com/jumbokh/DataScience_1082/blob/master/images/Figure_1.png)
        * ![圖二](https://github.com/jumbokh/DataScience_1082/blob/master/images/Figure_2.png)
 * [迴歸](regression.md)
    * [簡單迴歸](https://nbviewer.jupyter.org/github/jumbokh/DataScience_1082/blob/master/src/simple_regression.ipynb)
    * [05.06 Linear Regression](https://nbviewer.jupyter.org/github/jumbokh/regression_learn/blob/master/src/05.06-Linear-Regression.ipynb)
    * [判斷是哪個亞種的鳶尾花](https://nbviewer.jupyter.org/github/jumbokh/intro-computers/blob/master/src/0702%20%E5%88%A4%E6%96%B7%E6%98%AF%E5%93%AA%E5%80%8B%E4%BA%9E%E7%A8%AE%E7%9A%84%E9%B3%B6%E5%B0%BE%E8%8A%B1.ipynb)
    * [正則化參考](https://blog.csdn.net/jinping_shi/article/details/52433975)
        * [正則化Notebook](https://nbviewer.jupyter.org/github/jumbokh/intro-computers/blob/master/src/%E6%AD%A3%E5%89%87%E5%8C%96.ipynb)
    * [標準化 Notebook](https://nbviewer.jupyter.org/github/jumbokh/intro-computers/blob/master/src/standardizing_sequence.ipynb)
    * [Normalization Notebook](https://nbviewer.jupyter.org/github/jumbokh/intro-computers/blob/master/src/Normalizing_Sequence.ipynb)

* [深度學習](https://github.com/jumbokh/intro-computers/blob/master/DeepLearning.md)
    * [深度學習--ch3 Notebook](https://nbviewer.jupyter.org/github/jumbokh/DataScience_1082/blob/master/src/Ch03.ipynb)
* [雲端運算](https://github.com/jumbokh/intro-computers/blob/master/cloud.md)
    * 雲端平台 
        * Microsoft Azure
        * Google Cloud Platform

##

### Home Work
* HW1(3/12): 台電106統計年報 -- 附錄, 第232~233頁資料表 (國內經濟指標) 
* HW2(3/19): 請依高雄旅遊資料, 製作查詢報表。[高雄旅遊網-景點資料](https://data.gov.tw/dataset/47020) 
    * ![HW](https://github.com/jumbokh/DataScience_1082/blob/master/images/HW2.JPG)
* HW3(4/9): 以聚類範例二 immp-som.ipynb 為範本, 使用範例一之資料 (7,2)，試著執行分類
    * ![result](https://github.com/jumbokh/DataScience_1082/blob/master/images/SOM-out.JPG)
    * ![output1](https://github.com/jumbokh/DataScience_1082/blob/master/images/SOM-ex.png)
    * ![output2](https://github.com/jumbokh/DataScience_1082/blob/master/images/SOM-ex1.png)
* HW4(4/16): 以[optimizer selection](https://nbviewer.jupyter.org/github/jumbokh/hands-on-DL/blob/master/ex04_optimizer-selection.ipynb)程式為範本，使用 MNIST dataset (參照 [打造第一個神經網路](https://nbviewer.jupyter.org/github/yenlung/Deep-Learning-MOOC/blob/master/%E6%94%BF%E5%A4%A7%E8%81%B7%E6%B6%AF%E4%B8%AD%E5%BF%832019/%E6%89%93%E9%80%A0%E4%BA%BA%E7%94%9F%E7%AC%AC%E4%B8%80%E5%80%8B%E7%A5%9E%E7%B6%93%E7%B6%B2%E8%B7%AF.ipynb) 載入data的方式)
    * ![correct](https://github.com/jumbokh/DataScience_1082/blob/master/images/correct.JPG)
    * ![HW4](https://github.com/jumbokh/DataScience_1082/blob/master/images/HW4-optimizer.png)
* 問題挑戰範例
    * [應用開放資料預測農產品菜價之研究, 師範大學, 翟柏森](http://nccur.lib.nccu.edu.tw/handle/140.119/118330) [[pdf]](https://github.com/jumbokh/DataScience_1082/blob/master/data/paper.pdf) [[資料說明]](https://github.com/jumbokh/DataScience_1082/tree/master/examples) [感謝作者翟先生提供論文資料]
        * [線上發表會](http://knowledge.colife.org.tw/one_video/index.aspx?sid=10804)
        * [農產品交易開放資料](https://data.coa.gov.tw/Query/ServiceDetail.aspx?id=037)
        * [氣象開放資料](http://e-service.cwb.gov.tw/HistoryDataQuery/)
        * [颱風警報](https://rdc28.cwb.gov.tw/)
        * [論文取得資料](https://drive.google.com/open?id=14iT9UiWNZJcWD73wFn9aRUGqjW2hYvB7)
    * [新北市公共自行車租賃系統(YouBike)](https://data.ntpc.gov.tw/od/detail?oid=71CD1490-A2DF-4198-BEF1-318479775E8A)
        * ![reorginaze](https://github.com/jumbokh/DataScience_1082/blob/master/images/ubike-ex1.JPG)
        * ![reorginaze](https://github.com/jumbokh/DataScience_1082/blob/master/images/ubike.jpg)
    * [氣象局開放資料擷取](中央氣象局開放資料平臺之資料擷取API)
    * Kaggle 競賽：鐵達尼號 [(Titanic: Machine Learning from Disaster)](https://www.kaggle.com/c/titanic)
        * ![生存率--依性別](https://github.com/jumbokh/DataScience_1082/blob/master/images/Titantic-servial.JPG)
        * [All data](https://github.com/jumbokh/DataScience_1082/blob/master/data/titanic.zip)
        * [解題範例說明](https://medium.com/@yulongtsai/https-medium-com-yulongtsai-titanic-top3-8e64741cc11f)
        * [source code](https://nbviewer.jupyter.org/github/jumbokh/DataScience_1082/blob/master/src/Kaggle_Titanic_Top3__Medium.ipynb)
    * [Predicting Bicycle Traffic](https://github.com/DataScienceWorks/PredictingBicycleTraffic)
        * [Fremont Bridge Bicycle Counter](https://data.seattle.gov/Transportation/Fremont-Bridge-Bicycle-Counter/65db-xm6k)
##         
### 參考連結
* [github基本教學 - 從無到有](https://www.youtube.com/watch?v=py3n6gF5Y00&feature=youtu.be)
* [李宏毅老師--機器學習課程](http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html?fbclid=IwAR1KQwREtEHpCKeNNmiPa7uwYZITcMMag5xrc3PudXtTDG6Zf7aw-03fR6A)
* [iris-经典案例解析-机器学习](https://www.jianshu.com/p/da18f0cd7f60)
    * 見 7.5 做鳶尾花的分類
* [动手学深度学习](https://1024.com/a/279/%E4%B8%80%E6%9C%AC%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E7%9A%84%E5%A5%BD%E4%B9%A6dive-into-deep-learning-%E4%B8%AD%E8%8B%B1%E6%96%87)
    * 見 [3.1. 线性回归](https://zh.d2l.ai/chapter_deep-learning-basics/linear-regression.html)
* [機器學習算法導論](https://lib-nuanxin.wqxuetang.com/#/Book/3208845)
* [SGD, Momentum, AdaGrad, Adam Optimizer](https://mc.ai/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92ml-notesgd-momentum-adagrad-adam-optimizer-2/)
* [机器学习之路：python线性回归分类器 LogisticRegression SGDClassifier 进行良恶性肿瘤分类预测](https://www.cnblogs.com/Lin-Yi/p/8970510.html)
* [vs.code Download](https://code.visualstudio.com/)
* [Deeplearning Algorithms Tutorial ](https://github.com/KeKe-Li/tutorial)
* [李宏毅-- AI課程](http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html?fbclid=IwAR1KQwREtEHpCKeNNmiPa7uwYZITcMMag5xrc3PudXtTDG6Zf7aw-03fR6A)
* [蔡炎龍 政大磨課師](http://moocs.nccu.edu.tw/course/172/intro)
* [復旦大學：深度學習與神經網路, 邱錫鵬](https://nndl.github.io/) [[pdf]](https://nndl.github.io/ppt/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E4%B8%8E%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0-3%E5%B0%8F%E6%97%B6.pdf)
* [RealCalc Scientific Calculator](https://play.google.com/store/apps/details?id=uk.co.nickfines.RealCalc&hl=en_US)
* [What You Need to Know to Solve Your Data Puzzle](https://blog.cloudfactory.com/solve-your-data-puzzle?utm_campaign=RTQD%20%7C%20Email%20Nurture&utm_medium=email&_hsenc=p2ANqtz-_9VHlUd3BxZd5wrFzZqhNpzdYYdtLUQ4uJCHJkUZh87S6aQQ_BX-BIjudX2hV4WRjN3z0SCcK0HgRitg90k5LJ75P4kA&_hsmi=84864590&utm_source=hs_automation&utm_content=84864590&hsCtaTracking=2127cbf5-c61f-4601-a280-b23dcda3857a%7C96b40409-51a9-40eb-b270-7d9e1efa0dda)
##
### 書籍
* ![Power BI](http://www.gotop.com.tw/Waweb2004/WawebImages/BookXL/ACI031500.jpg)
    * [PowerBI 終極實戰寶典](http://books.gotop.com.tw/v_ACI031500#03)
##
* ![Python BigData](http://www.gotop.com.tw/Waweb2004/WawebImages/BookXL/ACL054700.jpg)
    * [Python 大數據資料分析](http://books.gotop.com.tw/v_ACL054700#)
##
* ![Python數據科學手冊](https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/151/72/CN11517291.jpg&v=5aca6204&w=348&h=348)
    * [Python數據科學手冊](https://www.books.com.tw/products/CN11517291)
* ![book1](https://github.com/jumbokh/intro-computers/blob/master/images/book1.png)
* [旗標-深度學習必讀](https://www.flag.com.tw/books/product/F9379)
* ![book2](https://github.com/jumbokh/intro-computers/blob/master/images/book2.png)
* [鴻海-人工智慧導論](https://www.books.com.tw/products/0010826415)
* ![book4](https://github.com/jumbokh/intro-computers/blob/master/images/book4.PNG)
* [前程文化-大數據分析與資料挖礦2/e](https://www.books.com.tw/products/0010815082)

