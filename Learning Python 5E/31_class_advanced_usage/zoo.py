#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class Animal:
	def speak(self):
		print('Animal')
	def reply(self):
		self.speak()
class Mammal(Animal):
	def speak(self):
		print('Mammal')
class Cat(Mammal):
	def speak(self):
		print('Cat meow')
class Dog(Mammal):
	def speak(self):
		print('Dog')
class Primate(Mammal):
	def speak(self):
		print('Hello World!')
class Hacker(Primate):
	pass
		
