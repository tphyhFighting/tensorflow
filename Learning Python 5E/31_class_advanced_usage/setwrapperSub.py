#!/usr/bin/env python
# --*-- coding:utf-8 --*--
from setwrapper import Set
class SetSub(Set):
	def intersect(self, *arg):
		res = []
		for x in self.data:
			for other in arg:
				if x not in other:
					break
			else:
				res.append(x)
		return Set(res)
	def union(*arg):
		res = []
		for other in arg:
			for x in other:
				if x not in res:
					res.append(x)
		return Set(res)
