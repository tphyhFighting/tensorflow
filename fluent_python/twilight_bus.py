#!/usr/bin/env python
# coding=utf8


class TwilightBus:
	def __init__(self, passengers=None):
		if passengers is None:
			self.passengers = []
		else:
			self.passengers = list(passengers)
	
	def pick(name):
		self.passengers.append(name)

	def drop(name):
		self.passengers.remove(name)
