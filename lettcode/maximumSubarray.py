#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		Sum = nums[0]
		maxnum = nums[0]
		for x in nums[1:]:
			if Sum < 0:
				Sum = 0
			Sum += x
			maxnum = max(Sum,maxnum)
		return maxnum
