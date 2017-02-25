#!/usr/bin/env python
# --*-- coding:utf-8 --*--
def print_all(s):
	if isinstance(s, int):
		print(s)
	elif isinstance(s, dict):
		for key in s:
			print(key,s[key])
	else:
		for x in s:
			print(x)
def func(x):
	print(x)
func([1,2,3,4])
