#!/usr/bin/env python
# -*- coding:utf-8 -*-
## Animal is a object(sort of confusing)look at the extra credit
class Animal(object):
    pass
    def run(self):
        print "I got called and I can run."
class Dog(Animal):
    def __init__(self,name):
        self.name = name
class Cat(Animal):
    def __init__(self,name):
        self.name = name
class Person(object):
    def __init__(self,name):
        self.name = name
        self.pet = None
class Employee(Person):
    def __init__(self,name,salary):
	super(Employee, self).__init__(name)
        self.salary = salary
class Fish(object):
    pass
class Salmon(Fish):
    pass
class Halibut(Fish):
    pass
## rover is-a Dog
rover = Dog("Rover")
## satan is-a Cat
satan = Cat("Satan")
## mary is-a Person
mary = Person("Mary")
mary.pet = satan
## frank is-a Employee
frank = Employee("Frank",12000)
frank.pet = rover
## flipper is-a Fish
flipper = Fish()
## crouse is-a Salmon
crouse = Salmon()
## harry is-a Halibut
harry = Halibut()

