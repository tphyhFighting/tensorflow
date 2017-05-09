#!/usr/bin/env python
# --*-- coding:utf-8 --*--
from pandas import Series,DataFrame
obj = Series([4, 7, -5, 3])
print "obj:", obj
print "obj.values:", obj.values
print "obj.index:", obj.index
obj2 = Series([4, 7, -5, 3], index = ['d', 'b', 'a', 'c'])
print "obj2:", obj2
print "obj2.index:", obj2.index
print "obj2['a']:", obj2['a']
obj2['d'] = 6
print "obj2[['c', 'a', 'd']]:", obj2[['c', 'a', 'd']]
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print "new_index_obj:", obj
