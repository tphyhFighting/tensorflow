#!/usr/bin/env python
# --*-- coding:utf-8 --*--
def adder(*args):
	sum = args[0]
	for x in args[1:]:
		print 'hello'
		sum += x
	return sum
#print adder('happ','iness')
#print adder([1,2],[3,4])
#print adder(2.5, 3.6)
#print adder(12,24)
print adder(10)
def adder_3(good = 1, bad = 2, ugly = 3):
	return good + bad + ugly
print adder_3()
print adder_3(1,3)
print adder_3(ugly = 1, good = 2)
def adder_all(**args):
	values = list(args.values())
	sum = values[0]
	for value in values:
		sum += value
	return sum
print(adder_all(ugly = 1, good = 2, bad = 3))
		
	
