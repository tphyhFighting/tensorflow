#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class Super(object):
	def method(self):
		print('in Super.method')
class Sub(Super):
	def method(self):
		print('Starting in Sub.method')
		Super.method(self)
		print('Ending in Sub.method')
x = Super()
x.method()
y = Sub()
y.method()
