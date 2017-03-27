#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class classic:
	def __getattr__(self, name):
		if name == 'age':
			return 40
		else:
			raise AttributeError
	def __setattr__(self, name, value):
		print('set:', name, value)
		if name == 'age':
			self.__dict__['_age'] = value
		else:
			self.__dict__[name] =value
x = classic()
print x.age
#print x.name
class newprops(object):
	def getage(self):
		return 40
	def setage(self, value):
		print('set age:', value)
		self._age = value
	age = property(getage, setage, None, None)
y = newprops()
print y.age
y.age = 42
print y._age
print y.age
y.job = 'trainer'
print y.job 
