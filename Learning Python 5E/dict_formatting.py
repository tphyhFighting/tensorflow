#!/usr/bin/env python
# -*- coding:utf-8 -*-
print('%(qty)d more %(food)s'%{'qty': 1, 'food': 'spam'})
reply = """
Greetings...
Hello %(name)s!
Your age is %(age)d
"""
values = {'name': 'Bob', 'age': 40}
print(reply % values)
