#!/usr/bin/env python
# --*-- coding:utf-8 --*--
def copyDict(D):
	newDict = {}
	for key in D:
		newDict[key] = D[key]
	return newDict
D = {1:'tp',2:'hyh'}
print(copyDict(D))
	
