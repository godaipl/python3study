#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

print('我是中国人')
print(ord("我"))
print(chr(ord("我")))
# print(bytes(b'我')) #会报异常
print("我".encode("UTF-8"))
# print("我".encode("ascii"))
print("我".encode("UTF-8").decode("UTF-8"))

# 格式化
print('HELLO %s' % '波波')
print('HELLO NO is %d' % 1)
print('HELLO Salary is %f' % 1.0)

print('HELLO %s , No is %d , Salary is %f' % ('波波', 1, 1.0))
