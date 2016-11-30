#!/usr/bin/python
#coding:utf-8

import os

cur_path = os.path.dirname(__file__)
print(cur_path)
cmd = 'mv {} /usr/bin/'.format(os.path.join(cur_path, 'tprm'))
print(cmd)
#os.sytem(cmd)
print('install ok')
