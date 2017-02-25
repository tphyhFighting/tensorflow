#!/usr/bin/env python
# --*-- coding:utf-8 --*--
def selectPrime(y):
	if y == 0 or y == 1:
		print(y, 'is not prime')
		return 
	x = y // 2
	while x > 1:
		if y % x == 0:
			print(y, 'has factor', x)
			break
		x -= 1
	else:
		print(y, 'is prime')
selectPrime(13)
selectPrime(13.0)
selectPrime(15)
selectPrime(15.0)
selectPrime(0)
selectPrime(1)
