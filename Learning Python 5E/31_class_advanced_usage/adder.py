#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class Adder(object):
	def __init__(self, start = []):
		self.data = start
	def __add__(self, y):
		return self.add(y)
	def add(self, y):
		print 'Not Implemented'
class ListAdder(Adder):
	def add(self, y):
		return self.data + y
class DictAdder(Adder):
	def add(self, y):
		new = {}
		for k in self.data: new[k] = self.data[k]
		for k in y: new[k] = y[k]
		return new
x = ListAdder([1,2,3])
y = x + [4,5,6]
print y
dic = DictAdder({1:1})
dic1 = dic + {2:2}
print dic1
