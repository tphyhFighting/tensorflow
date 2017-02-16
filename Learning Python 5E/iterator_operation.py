#!/usr/bin/env python
# --*-- coding:utf-8 --*--
#python中的迭代环境包括：for循环，列表解析，map内置函数，in成员关系测试表达式
for x in [1,2,3,4]:
	print(x ** 2),
for x in 'spam':
	print(x * 2),
#文件迭代器
for line in open('script1.py'):
	print(line.upper()), #Calls __next__,catches StopIteration
for line in open('script1.py').readlines():
	print(line.upper()), #文件的readlines方法，将文件内容加载到内存
D = {'a':1, 'b':2, 'c':3}
for key in D.keys():
	print(key, D[key])
#列表解析
L = [1,2,3,4,5]
L = [x + 10 for x in L]
print(L)
#扩展的列表解析
lines = [line.rstrip() for line in open('script1.py') if line[0] == 'p']
print(lines)
#下列for循环也可以达到列表解析的效果
M = [1,2,3,4,5]
res = []
for x in M:
	res.append(x + 10)
print(M)
#sum,any,all,max,min内置函数对于可迭代对象的作用
print(sum([3,2,4,1,5,0]))
print(any(['spam','','ni']))
print(all(['spam','','ni']))
print(max([3,2,5,1,4]))
print(min([3,2,5,1,4]))
#字典解析表达式
Dict = {ix:line for ix, line in enumerate(open('script1.py'))}
#filter内置函数
print(list(filter(bool,['spam','','ni'])))
