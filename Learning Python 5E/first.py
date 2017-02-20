#!/usr/bin/env python
# --*-- coding:utf-8 --*--
#在文件间进行通信最好的办法就是通过调用函数，传递参数，然后得到其返回值
x = 99
def setX(new):
	global x
	x = new
