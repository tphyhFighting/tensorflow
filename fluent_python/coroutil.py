#!/usr/bin/env python
# --*-- coding:utf-8 --*--
from functools import wraps
def coroutine(func):
	print("start")
	@wraps(func)
	def primer(*arg, **kwargs):
		print("in primer")
		gen = func(*arg, **kwargs)
		next(gen)
		print("return gen")
		print('gen:', gen)
		return gen
	print("return primer")
	return primer
