#!/usr/bin/env python
# coding=utf-8
import collections
Event = collections.namedtuple('Event', 'time proc action')
def taxi_process(ident, trips, start_time = 0):
	time = yield Event(start_time, ident, 'leave garge')
	for i in range(trips):
		time = yield Event(time, ident, 'pick up passenger')
		time = yield Event(time, ident, 'drop off passenger')
	
	yield Event(time, ident, 'going home')
