#coding=utf-8
'''
Created on 2016.12.25
Top Quant-极宽量化分析系统
培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com
'''


#-----------------------------------------------------------------------------------
dss='hello ziwang.com'
print('dss',dss)

#1
# 从左到右索引默认0开始，最大长度是字符串长度减1；
# 从有到左索引默认-1开始，最大范围是字符串开头。
# 下标为空，表示取到头或尾。
print('\n#1')
s2=dss[1:];print('s2,',s2)
s3=dss[1:3];print('s3,',s3)
s4=dss[:3];print('s4,',s4)

#2
print('\n#2')
s2=dss[-1];print('s2,',s2)
s3=dss[1:-2];print('s3,',s3)
dn=len(dss);print('dn,',dn)

#3
print('\n#3')
print('s2+s3,',s2+s3)
print('s3*2,',s3*2)


