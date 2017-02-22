#!/usr/bin/env python
# --*-- coding:utf-8 --*--
def knights():
	title = 'Sir'
	action = (lambda x: title + ' ' +x)
	return action
act = knights()
print act('robin')
L = [lambda x: x ** 2,lambda x: x ** 3,lambda x: x ** 4]
for f in L:
	print(f(2))
print(L[0](3))
