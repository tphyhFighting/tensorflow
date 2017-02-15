#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''while loop'''
x = 'spam'
while x:
	print(x),
	x = x[1:]
a = 0; b = 10
while a < b:
	print(a),
	a += 1
'''continue'''
nu = 10
while nu:
	nu -= 1
	if nu % 2 != 0:continue
	print(nu),
'''break'''
while True:
	name = input('Enter name:')
	if name == 'stop':break
	age = input('Enter age:')
	print('Hello',name,'=>',int(age))
'''for loop'''
for st in ["spam","eggs","ham"]:
	print(x),
S = "lumberjack"
for item in S:
	print(item),
print(list(range(5, -5, -1)))
L1 = [1,2,3,4]
L2 = [5,6,7,8]
print(list(zip(L1,L2)))
'''enumerate'''
St = 'spam'
for (offset, item) in enumerate(St):
	print(item, 'appears at offset',offset)
