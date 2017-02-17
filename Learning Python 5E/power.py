#!/usr/bin/env python
# --*-- coding:utf-8 --*--
L = []
for x in xrange(7):
	L.append(2 ** x)
print L
X = 5
#found = False
dst = 2 ** 5
if dst in L:
	print('at index',L.index(dst))
else:
	print(X, 'not found')
