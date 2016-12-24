#!/usr/bin/env python
# -*- coding:utf-8 -*-
while True:
	reply = input('Enter text:')
	if reply == 'stop':
		break
	elif not reply.isdigit():
		print('Bad!' * 8)
	else:
		num = int(reply)
		if num < 20:
			print('Too low!')
		else:
			print(num ** 2)
	#else:
	#	print(int(reply) ** 2)
print('Bye')
