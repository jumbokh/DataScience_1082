import pandas as pd

bmi_data = {
            "Name" : ['Ron', 'Jerry', 'Nick', 'Andy', 'Masour'],
            "Height" : [173, 175, 173, 178, 174],
            "Weight" : [60, 95, 70, 55, 58]
           }

df = pd.DataFrame(bmi_data, columns=bmi_data.keys())
print('原始資料：\n', df)
print()

#給每一筆原始資料計算BMI
BMI = (df['Weight'] / (df['Height']/100)**2).map('{:,.2f}'.format)
#獲得每一筆BMI狀態
state = []
for bmi in BMI.values:
    bmi = eval(bmi)
    if bmi < 18.5:
        state.append('過輕')
    elif 18.5 <= bmi < 24:
        state.append('正常')
    elif 24 <= bmi < 27:
        state.append('過重')
    else:
        state.append('肥胖')
BMI_with_state = {'BMI' : BMI, 'State' : state}
BMI_df = pd.DataFrame(BMI_with_state, columns=BMI_with_state.keys()) 

#將BMI資料加入原始資料
df = df.join(BMI_df)

print('加入BMI後：\n', df)
print()

print('肥胖者：\n', df[df['State'] == '肥胖'])