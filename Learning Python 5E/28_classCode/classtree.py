#!/usr/bin/env python
# --*-- coding:utf-8 --*--
"""
Climbing inheritance trees using namespace links,
displaying higher superclasses with indentation
"""
def classtree(cls, indent):
	print('.' * indent + cls.__name__)
	for supercls in cls.__bases__:
		classtree(supercls, indent + 3)
def instancetree(inst):
	print('Tree of %s' %inst)
	classtree(inst.__class__, 3)
