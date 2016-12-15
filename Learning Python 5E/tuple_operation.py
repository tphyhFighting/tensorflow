#!/usr/bin/env python
# -*- coding:utf-8 -*-
T = (1,2,3,4)
print('len(T)',len(T))
print('T + (5,6)',T + (5,6))
print('T[0]',T[0])
print('T.index(4)',T.index(4))
print('T.count(4)',T.count(4))
T = (2,) + T[1:]
print('new tuple T',T)
