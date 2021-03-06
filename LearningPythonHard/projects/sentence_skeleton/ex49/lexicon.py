#!/usr/bin/env python
# -*- coding:utf-8 -*-
class ParserError(Exception):
    pass
class Sentence(object):
    def __init__(self,subject,verb,objec):
        self.subject = subject[1]
        self.verb = verb
        self.objec = objec[1]
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None
def match(word_list,excepting):
    if word_list:
        word = word_list.pop(0)
        if word[0] == excepting:
            return word
        else:
            return None 
    else:
        return None
def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list,word_type)
def parse_verb(word_list):
    skip(word_list,'stop')
    if peek(word_list) == 'verb':
        return match(word_list,'verb')
    else:
        raise ParserError("Excepted a verb next.")
def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)
    if next == 'noun':
        return match(word_list,'noun')
    if next == 'direction':
        return match(word_list,'direction')
    else:
        raise ParserError("Excepted a noun or direction next.")
def parse_subject(word_list,subj):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    return Sentence(subj,verb,obj)
def parse_sentence(word_list):
    '''
    >>> parse_sentence([('verb','eat'),('stop','the'),('noun','bear')])#doctest: +ELLIPSIS
    <lexicon.Sentence object at 0x...>
    '''
    skip(word_list,'stop')
    start = peek(word_list)
    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list,subj)
    elif start == 'verb':
        return parse_subject(word_list,('noun','player'))
    else:
        raise ParserError("Must start with subject,object or verb not:%s"% start)   

