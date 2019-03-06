# -*- coding: utf-8 -*-
s = 'how are you'
#s被赋值后就是一个字符串类型的对象
l = s.split()
#split是字符串的方法，这个方法返回一个list类型的对象
#l是一个list类型的对象
print l

#通过dir()方法可以查看一个类/变量的所有属性：
print dir(s)
print dir(list)
