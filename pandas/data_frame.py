#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import numpy as np
import pandas as pd
dates = pd.date_range('20170428', periods = 6)
df = pd.DataFrame(np.random.randn(6, 4), index = dates, columns=list('ABCD'))
print "df :", df
df2 = pd.DataFrame({'A':np.random.randn(6)})
print "df2 :", df2
df3 = pd.DataFrame({'A':pd.Timestamp('20170511'),'B':pd.Series(1)})
print "df3 :", df3
df4 = pd.DataFrame({'A':pd.Timestamp('20170510'),'B':pd.Series(1, index=list(range(4)))})
print "df4 :", df4
print "df.head():",df.head()
print "df.tail():",df.tail()
print "df.describe():",df.describe()
print "df.T:", df.T
print "after sort columns C:",df.sort(columns = "C") 
