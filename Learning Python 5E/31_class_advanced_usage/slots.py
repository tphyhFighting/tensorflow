#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class D(object):
	__slots__ = ['a','b','__dict__']
	c = 3
	def __init__(self): self.d = 4
x = D()
x.b = 2
x.a = 1
print(getattr(x, 'a'), getattr(x, 'c'), getattr(x, 'd'))
for attr in list(getattr(x, '__dict__')) + getattr(x, '__slots__'):
	print(attr, '=>', getattr(x, attr))
