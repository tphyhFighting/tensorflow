#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from sys import argv
script= argv
print "I'm going to read your file.Please enter your filename",
file_name = raw_input(">")
txt = open(file_name)
print txt.read()

