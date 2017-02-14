#!/usr/bin/env python
# -*- coding:utf-8 -*-
x = 'killer rabbit'
if x == 'roger':
	print("how's jessica?")
elif x == 'bugs':
	print("what's up doc?")
else:
	print('Run away! Run away!')

choice = 'bacon'
branch = {'spam':1.25,'ham':1.99,'eggs':0.99}
if choice in branch:
	print(branch[choice])
else:
	print('Bad choice!')

s = 'SPAM'
if 'rubbery' in 'shrubbery':
	print(s * 8)
	s += 'NI'
	if s.endswith('NI'):
		s *= 2
		print(s)
