#!/usr/bin/env python
# -*- coding:utf-8 -*-
from game import Game
class LoveRoom(object):
    def __init__(self,f,m):
        self.__fname = f
        self.__mname = m
    def warning(self):
        '''You are entering a magic room.
    If you think you a good guy,you can enter.
        Before you enter,you have to answer some questions.
        '''
        print "The room is owed by %s and %s"%(self.__fname,self.__mname)
        answer1 = raw_input("Do you have a girlfriend or boyfriend?Please enter yes or no:")
        if answer1 == 'yes':
            print "There may be a beautiful and sex girl,you can choose go forward or go back"
            answer2 = raw_input("please enter forward or back:")
            if answer2 == "forward":
                print "Sorry,you are out"
            elif answer2 == "back":
                print "ok,you can safely go back"
            else:
                print "DOES NOT COMPUTE!"
        else:
            print "You may play some games to let a beautiful girl as your wife."
            num = raw_input("You can choose games by the numbers(1):")
            if num == '1':       
                #answ = game[0]
                #print "1"
                ga = Game()
                ga.answer1()
            else:
                print "Please enter number 1"
            
love = LoveRoom('tp','hyh')
love.warning()


       
        

    
