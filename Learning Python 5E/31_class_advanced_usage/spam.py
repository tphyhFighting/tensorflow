#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class Spam:
	numInstances = 0
	def __init__(self):
		Spam.numInstances = Spam.numInstances + 1
	def printNumInstances():
		print("Number of instances created:", Spam.numInstances)
	printNumInstances = staticmethod(printNumInstances)
	def printNumInstances_cls(cls):
		print("Number of instances created:",cls.numInstances)
	printNumInstances_cls = classmethod(printNumInstances_cls)
a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances_cls()
a.printNumInstances_cls()
