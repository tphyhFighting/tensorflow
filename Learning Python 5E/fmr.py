#!/usr/bin/env python
# --*-- coding:utf-8 --*--
#map
def inc(x): return x + 10
counters = [1, 2, 3, 4]
print(list(map(inc,counters)))
#filter
print(list(filter((lambda x: x > 0),range(-5, 5))))
#reduce
print(reduce((lambda x, y: x * y),[1,2,3,4]))
