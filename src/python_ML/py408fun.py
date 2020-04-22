#coding=utf-8
'''
Created on 2016.12.25
Top Quant-极宽量化分析系统
培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com
'''

#------------------
def f01(a,b,c):
    print('a,b,c,',a,b,c)
    a2,b2,c2,=a+c,b*2,c*2
    #
    return a2,b2,c2
#    

#1
print('\n#1')
x,y,z=f01(1,2,3)
print('x,y,z,',x,y,z)

#2
print('\n#2')
x,y,z=f01(x,y,z)
print('x,y,z,',x,y,z)