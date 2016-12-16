#!/usr/bin/env python
# -*- coding:utf-8 -*-
print('int(3.1415):',int(3.1415))
print('float(3):',float(3.0))
#classic division
print('classic division 4.0/5',4.0/5)
#floor division
print('floor division 5//4',5//4)
#numbers => digit strings
print('oct(64),hex(64),bin(64)',oct(64),hex(64),bin(64))
import random
print('random.random():',random.random())
from decimal import Decimal
de = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print('Decimal de',de)
