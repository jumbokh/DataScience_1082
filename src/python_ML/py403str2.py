#coding=utf-8
'''
Created on 2016.12.25
Top Quant-极宽量化分析系统
培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com
'''


#------------------


#1
dss='  hello ziwang.com,,'
print('\n#1,去空格及特殊符号')
s2=dss.strip().lstrip().rstrip(',')
print('s2,',s2)

#2
print('\n#2,字符串连接')
s2=dss.join(['a','.','c'])
print('s2,',s2)
s3='s3'
s3+='xx'
print('s2,',s3)

#3
print('\n#3,查找字符')
css='abc1c2c3'
pi=css.find('c')
print('pi,',pi)

#4
print('\n#4,字符串比较')
s1='abc'
s2='c123'
print('s1>s2',s1>s2)
print('s1==s2',s1==s2)
print('s1<s2',s1<s2)

#5
print('\n#5,字符串长度')
s1,s2='abc','c123'
print('len(s1),',len(s1))
print('len(s2),',len(s2))

#6
print('\n#6,大小写转换')
s1,s2='abc','ABC123efg'
print('大写，s1.upper(),',s1.upper())
print('小写，s2.lower(),',s2.lower())
print('大小写互换 ,s2.swapcase(),',s2.swapcase())
print('首字母大写 ,s1.capitalize(),',s1.capitalize())

#7
print('\n#7,分割字符串')
s2='  hello, ziwang,com,,'
print('s2.split,',s2.split(','))






























