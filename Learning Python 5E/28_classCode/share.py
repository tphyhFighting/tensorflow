#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class ShareData(object):
	spam = 42
x = ShareData()
y = ShareData()
print x.spam,y.spam
ShareData.spam = 92 #通过类名称修改spam
print x.spam,y.spam,ShareData.spam
