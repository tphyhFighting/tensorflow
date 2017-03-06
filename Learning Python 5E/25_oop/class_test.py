#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class C1(object):
	def setname(self, who):
		self.name = who
I1 = C1()
I1.setname('bob')
print(I1.name)
class Employee(object):
	def __init__(self, who):
		self.name = who
	def computeSalary(self):	pass
	def giveRaise(self):	pass
	def promote(self):	pass
	def retire(self):	pass
class Engineer(Employee):
	def computeSalary(self):	pass
bob = Employee('bob')
mel = Engineer('mel')
company = [bob, mel]
for emp in company:
	print(emp.computeSalary())
