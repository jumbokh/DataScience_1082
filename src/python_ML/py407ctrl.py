#coding=utf-8
'''
Created on 2016.12.25
Top Quant-极宽量化分析系统
培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com
'''

#------------------
#1
print('\n1,if')
x,y,z=10,20,5
if x>y:
    print('x>y')
else:
   print('x<y') 
   
   
#2
print('\n#2,elif')
x,y,z=10,20,5
if x>y:
    print('x>y')
elif x>z:
   print('x>z') 
   
#3
print('\n#3,whiel')
x=3
while x>0:
    print(x)
    x-=1

#4
print('\n#4,for')
xlst=['1','b','xxx']
for x in xlst:
    print(x)
       
#5
print('\n#5,for')
for x in range(3):
    print(x)
    