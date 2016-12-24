#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution(object):
	def addDigits(self, num):
			while num > 9:
				c = 0
				while num:
					c += num % 10
					num /= 10
				num = c
			return num
s = Solution()
print s.addDigits(234)
print s.addDigits(9)
print s.addDigits(38)
