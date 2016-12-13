#!/usr/bin/env python
# -*- coding:utf-8 -*-
L = [123,'spam',1.23]
print('L length',len(L))
L.append('NI')
print('L_append',L)
print ('L_pop',L.pop(2))
M = ['bb','aa','cc']
M.sort()
print('M_sort',M)
M.reverse()
print('M_reverse',M)
N = [[1,2,3],[4,5,6],[7,8,9]]
col2 = [row[1] for row in N]
print('N_col_2',col2)
col2_1 = [row[1] + 1 for row in N]
print('N_col_2 + 1',col2_1)
col2_2 = [row[1] for row in N if row[1] % 2 == 0]
print('N_col_2 % 2',col2_2)
diag = [N[i][i] for i in [0,1,2]]
print('N_diag',diag)
doubles = [c * 2 for c in 'spam']
print('doubles',doubles)
print('list(range(-6, 7, 2))',list(range(-6,7,2)))
print('x**2,x**3',[[x**2,x**3] for x in range(4)])
print([[x,x/2,x*2] for x in range(-6,7,2) if x > 0])
G = (sum(row) for row in N)
print('next G',next(G))
print('list_map',list(map(sum, N)))
print('dict',{i : sum(N[i]) for i in range(3)})
print('dict_ord',{x:ord(x) for x in 'spaam'})
