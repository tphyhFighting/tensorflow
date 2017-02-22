#!/usr/bin/env python
# --*-- coding:utf-8 --*--
def mysum(L):
	if not L:
		return 0
	else:
		return L[0] + mysum(L[1:])
print(mysum([1,2,3,4,5,6]))
'''def mysum3(L):
	first, *rest = L
	return first if not rest else first + mysum3(rest)'''
#间接递归
def mySum(L):
	if not L: return 0
	return nonempty(L)
def nonempty(L):
	return L[0] + mySum(L[1:])
print(mysum([1,2,3,4,5,6]))
#while循环
L = [1,2,3,4,5,6]
Sum = 0
while L:
	Sum += L[0]
	L = L[1:]
print Sum
#for循环
suM = 0
T = [1,2,3,4,5,6]
for i in T:
	suM += i
print suM
	
