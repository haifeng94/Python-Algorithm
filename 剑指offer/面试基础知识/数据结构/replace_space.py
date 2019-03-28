#coding=utf-8
'''
题目：把字符串中的空格替换成'20%'
'''

#方法一：使用Python内置函数——replace
res1 = ' a  b  '.replace(' ', '20%')

#方法2: 使用正则表达式
import re
ret = re.compile(' ')
res2 = ret.sub('20%', ' a  b  ')
