#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class Commuter(object):
	def __init__(self, val):
		self.val = val
	def __add__(self, other):
		print('add', self.val, other)
		return self.val + other
	def __radd__(self, other):
		print('radd', self.val, other)
		return other + self.val
x = Commuter(88)
y = Commuter(99)
print(x + 1)
print(1 + y)
print(x + y)

