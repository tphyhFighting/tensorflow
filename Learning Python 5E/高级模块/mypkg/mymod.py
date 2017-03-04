#!/usr/bin/env python
# --*-- coding:utf-8 --*--
print("I'm ",__name__)
def countLines(f):
	f.seek(0)
	lines = len(f.readlines())
	return lines
def countChars(f):
	f.seek(0)
	chars = len(f.read())
	return chars
def test(name):
	f = open(name)
	print(countLines(f))
	print(countChars(f))
if __name__ == '__main__':
	test('mymod.py')
