#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sys import argv
script,user_name,host= argv
prompt = '>>'
print "Hi %s,I'm the %s script"%(user_name,script)
print "Today ,the %s host is not here,I'm the host now"%host
print "I'd like to ask you some questions."
print "Do you like me %s?"%user_name
likes = raw_input(prompt)
print "Where do you live %s?"%user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print """
Alright,so you said %r about liking me.
You live in %r.Yeah,it is a good place.
And you have a %r computer.Nice.
"""%(likes,lives,computer)
