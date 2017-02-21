#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# **特性只对关键字参数有效
'''
python内部是使用以下的步骤来在赋值前进行参数匹配的：
1: 通过位置分配非关键字参数
2: 通过匹配变量名分配关键字参数
3: 其他额外的非关键字参数分配到*name元组中
4: 其他额外的关键字参数分配到**name字典中
5: 用默认值分配给在头部未得到分配的参数
'''
def f(**args):
	print(args)
f()
f(a = 1, b = 2)
#函数头部能够混合一般参数，*参数以及**去实现更加灵活的调用方式
def f1(a, *pargs, **kargs):
	print(a, pargs, kargs)
f1(1, 2, 3, x = 1, y = 2)
#解包参数
def func(a, b, c, d):
	print(a,b,c,d)
args = (1, 2)
args += (3,4)
func(*args)
kargs = {'a': 1, 'b': 2, 'c': 3}
kargs['d'] = 4
func(**kargs)
func(1,c = 3,*(2,), **{'d':4})
