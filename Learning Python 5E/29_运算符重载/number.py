#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class Number(object):
	def __init__(self, start):
		self.data = start
	def __sub__(self, other):
		return Number(self.data - other)
class Indexer(object):
	data = [5,6,7,8,9]
	def __getitem__(self, index):
		print('getitem:', index)
		return self.data[index]
X = Indexer()
print X[0] #索引
print X[2:4] #分片
