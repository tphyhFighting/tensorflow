#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class MyError(Exception):
	pass
def stuff(file):
	raise MyError()
file = open('data', 'w')
try:
	stuff(file)
finally:
	file.close()
print('not reached')
