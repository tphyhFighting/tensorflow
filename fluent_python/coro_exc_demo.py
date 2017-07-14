#!/usr/bin/env python
# --*-- coding:utf-8 --*--
class DemoException(Exception):
	pass
def demo_exc_handling():
	print('-> coroutine started')
	try:
		while True:
			try:
				x = yield
			except DemoException:
				print('*** DemoException handled. Continuing...')
			else:
				print('-> coroutine received:{!r}'.format(x))
	finally:
		print('-> coroutine ending')
	raise RuntimeError('This line should never run.')
