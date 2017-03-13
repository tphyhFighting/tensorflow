#!/usr/bin/env python
# --*-- coding:utf-8 --*--
#python3.0
from abc import ABCMeta,abstractmethod
class Super(self):
	def delegate(self):
		self.action()
	@abstractmethod
	def action(self):
		pass
class Sub(Super):
	def action(self):
		print('spam')
X = Sub()
X.delegate()


