#!/usr/bin/env python
# -*- coding:utf-8 -*-
#direction = ('north','south','east','west','down','up','left','right','back')
#verb = ('go','stop','kill','eat')
#stops = ('the','in','of','from','at','it')
#noun = ('door','bear','princess','cabinet')
sentence_all = (('direction','north'),('direction','south'),('direction','east'),('direction','west'),('direction','down'),('direction','up'),('direction','left'),
('direction','right'),('direction','back'),('verb','go'),('verb','stop'),('verb','kill'),('verb','eat'),('stop','the'),('stop','in'),('stop','of'),('stop','from'),
('stop','at'),('stop','it'),('noun','door'),('noun','bear'),('noun','princess'),('noun','cabinet'))
#stuff = raw_input(">")
def scan(stuff):
    result = []
    flag = False
    words = stuff.split() 
    #print 'words',words
    for word in words:
        for tup in sentence_all:
            if word == tup[1]:
                result.append((tup[0],word))
                flag = True
        if flag == True:
            flag = False
            continue
        else:      
            s = convert_number(word)
            if s == None:
                result.append(('error',word))
            else:
                result.append(('number',s))
    return result
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

#rt = scan(raw_input(">"))
#print rt
