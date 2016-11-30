#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Game(object):
    def __init__(self):
        print "Game init"
    def answer1(self):
        print "You must answer me a question."
        print "Did you ever seen a long hair lady in the river showering,but you didn't see her face exactly."
        answ1 = raw_input("Please answer y or n:")
        if answ1 == 'y':
            print "You are the one the princess wants to find,and you find the yong lady is our princess,hope you be happy."
            print "You must answer one more queation"
            g = Game()
            g.answer2()
        elif answ1 == 'n':
            print "sorry, you can go back your home,hope you be happy."
        else:
            print "Please enter y or n"
            Game().answer1()
    def answer2(self):
        print "Why do you want to go there?"
        print "Do you fall in love with our princess"
        answ2 = raw_input("Please answer yes or no:")
        if answ2 == 'yes':
            print "a good ending"
            print "Now you can marry with our princess."
        elif answ2 == 'no':
            print "OK,fine.Now you can go where you want"
