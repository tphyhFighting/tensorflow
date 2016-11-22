#!/usr/bin/env python
# -*- coding:utf-8 -*-
mylist = [1,2,3,4]
print "mylist_bef",mylist
del mylist[0]
print "mylist_aft",mylist
#assert 2 + 2 == 3 + 3,"2+2 is not equal to 3+3"
def constructor():
    mylist = range(3)
    for i in mylist:
        yield i*i
myConstructor = constructor()
for i in myConstructor:
    print i
#print myConstructor


try:
    x = 1
    y = 2
    z = x + y
    #return z
    #return 'try'
    raise Exception('hello')
    print z
except Exception:
    print "process error."
finally:
    print "finally"

sum = lambda x,y:x + y
print "sum:",sum(2,4)
mul = lambda x, y:x * y
print "mul:",mul(1,3)


def Constructor1():
    x = 1
    y = 5
    z = x + y
    yield z

myConstructor1 = Constructor1()
print myConstructor1

