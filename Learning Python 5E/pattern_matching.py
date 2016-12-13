#!/usr/bin/env python
# -*- coding:utf-8 -*- 
import re
match = re.match('Hello[ \t]*(.*)world','Hello	Python world')
print match.group(1)
print match.groups()
match_1 = re.match('[/:](.*)[/:](.*)[/:](.*)','/usr/home:lumberjack')
print match_1.groups()
print re.split('[/:]','/usr/home/lumberjack')

