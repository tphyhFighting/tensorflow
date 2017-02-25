#!/usr/bin/env python
# --*-- coding:utf-8 --*--
def addDict(dict1, dict2):
	dict1keys = dict1.keys()
	#print dict1keys
	for key in dict2:
		if key not in dict1keys:
			dict1[key] = dict2[key]
	return dict1
dict1 = {'tp': 1,'hyh':2,'smile':3}
dict2 = {'happiness': 6,'love': 10,'smile':3}
print addDict(dict1,dict2)
def add_Dict(dict1, dict2):
	new = {}
	for key in dict1:
		new[key] = dict1[key]
	for key in dict2:
		new[key] = dict2[key]
	return new
print add_Dict(dict1,dict2)
		
	
			
