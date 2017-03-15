#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class Wrapper(object):
	def __init__(self, object):
		self.wrapped = object
	def __getattr__(self, attrname):
		print('Trace:', attrname)
		return getattr(self.wrapped, attrname)
