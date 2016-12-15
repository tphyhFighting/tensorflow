#!/usr/bin/env python
# -*- coding:utf-8 -*-
D = {'food':"Spam",'quality':4,'color':'pink'}
D['quality'] += 1
print('D[quality] +1:',D)
bob = {'name':'Bob','job':'dev','age':40}
bob1 = dict(name= 'Bob',job= 'dev',age= 40)
bob2 = dict(zip(['name','job', 'age'],['Bob','dev',40]))
rec = {'name':{'first': 'Bob','last': 'Smith'},'job': ['dev','mgr'],'age': 40.5}
print('rec[name]:', rec['name'])
print('rec[name][last]:',rec['name']['last'])
print('rec[job]:',rec['job'])
print('rec[job][-1]',rec['job'][-1])
rec['job'].append('janitor')
print('rec append janitor',rec['job'].append('janitor'))
Da = {'a': 1,'b': 2, 'c': 3}
print('Da:',Da)
Da['e'] = 99
print('Da assign new keys grows dict',Da)
print('f in Da','f' in Da)
if not 'f' in Da:
	print('missing')
if not 'f' in Da:
	print('missing')
	print('no, really ...')
print('Da.get(x, 0)',Da.get('x', 0))
value = Da['x'] if 'x' in Da else 0
print('value default zero',value)
Ks = list(Da.keys())
print('Da.keys before sorted',Ks)
Ks.sort()
print('Da.keys after sorted',Ks)
for key in Ks:
	print(key, '=>', Da[key])
for key in sorted(Da):
	print(key,'=>',Da[key])
x = 4
while x > 0:
	print('spam!' * x)
	x -= 1
print([x ** 2 for x in [1,2,3,4]])

