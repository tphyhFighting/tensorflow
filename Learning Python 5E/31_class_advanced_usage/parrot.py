#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class Actor:
	def line(self):
		print(self.name + ':', repr(self.says()))
class Scene:
	def __init__(self):
		self.clerk = Clerk()
		self.customer = Customer()
		self.subject = Parrot()
	def action(self):
		self.customer.line()
		self.clerk.line()
		self.subject.line()
class Customer(Actor):
	name = 'customer'
	def says(self):
		return "that's one ex-brid!"
class Clerk(Actor):
	name = 'clerk'
	def says(self):
		return "no it isn't ..."
class Parrot(Actor):
	name = 'parrot'
	def says(self):
		return None
