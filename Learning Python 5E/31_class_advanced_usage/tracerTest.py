#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class Tracer:
	def __init__(self, func):
		self.calls = 0
		self.func = func
	def __call__(self, *args):
		self.calls += 1
		print('call %s to %s' %(self.calls, self.func.__name__))
		self.func(*args)
@Tracer
def spam(a, b, c):
	print(a, b, b)
spam(1, 2, 3)
spam('a', 'b', 'c')
spam(4, 5, 6)
def deco(func):
	def _deco(a, b):
		print("before myfunc() called.")
		ret = func(a, b)
		print("		after myfunc() called. result: %s"%ret)
		return ret
	return _deco

@deco
def myfunc(a, b):
	print("	myfunc(%s, %s) called."%(a, b))
	return a + b
myfunc(1,2)
