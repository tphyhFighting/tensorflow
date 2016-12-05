#!/usr/bin/env python
# -*- coding:utf-8 -*-
from nose.tools import *
from ex49 import lexicon
import unittest
#print lexicon.scan("north")
class TestSentence(unittest.TestCase):
    def test_sentence_noun(self):
        lexicon.parse_sentence([('verb','eat'),('stop','the'),('noun','bear')])
        if self.assertRaises(lexicon.ParserError):
            print "ok,here is a error!"
