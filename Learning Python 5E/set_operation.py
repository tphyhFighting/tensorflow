#!/usr/bin/env python
# -*- coding:utf-8 -*-
X = set('spam')
Y = {'h','a','m'}
print('X,Y',X, Y)
print('X&Y',X&Y)#Intersection
print('X | Y',X | Y)#Union
print('X - Y',X - Y)#Difference
print('X > Y',X > Y)#Superset
print({n ** 2 for n in [1,2,3,4]})
print('set(spam) - set(ham)',set('spam') - set('ham'))
print('set(spam) == set(asmp)',set('spam') == set('asmp'))
import decimal
d = decimal.Decimal('3.141')
d += 1
print('d',d)
decimal.getcontext().prec = 3
print('pres 3:',decimal.Decimal('1.00') / decimal.Decimal('3.00'))
from fractions import Fraction
f = Fraction(2,3)
print('f + 1',f + 1)
print('f + Fraction(1, 2)',f + Fraction(1, 2))
print('bool(spam)',bool('spam'))
x = None
print('x',x)
L = [None] * 100
print('L', L)
