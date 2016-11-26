#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sys import exit
from random import randint
def death():
    quips = ["You died. You kinda suck at this.", "Nice job,you died ...jackass.", "Such a loser.", "I have a small puppy that's better at this."]
    print quips[randint(0,len(quips)-1)]
    exit(1)
def central_corridor():
    '''The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew. 

    You are the last surviving member and your last
    mission is to get the neutron destruct bomb from the Weapon Armory,
    put it in the bridge, and blow the ship up after getting into an "
    escaped pod.

    You're running down the central corridor to the Weapon Armory when
    a Gothon jumps out,red scaly skin, dark grimy teeth, and evil clown costume
    flowing around his hate filled body. He's blocking the door to the 
    Armory and about to pull a weapon to blast you.'''
    print central_corridor.__doc__
    action = raw_input('>')
    if action == "shoot!":
        '''Quick on the draw you yank out your blaster and fire it at the Gothon.

        His clown costume is flowing and moving around his body, which throws
        off your aim. Your laser hits his costume but misses his entirely. This
        completely ruins his brand new costume his mother bought him, which
        makes him fly into an insane range and blast you repeatedly in the face until
        you are dead. Then he eats you.'''
        return 'death'
    elif action == "dodge!":
        '''Like a world class boxer you dodge,slip and slide right
        as the Gothon's blaster cranks a laser past your head.
        In the middle of your artful dodge your foot slips and you
        bang your head on the metal wall and pass out.
        You wake up shortly after only to die as the Gothon stomps on
        your head and eats you.'''
        return "death"
    elif action == "tell a joke":
        '''lucky for you they made you learn Gothon insults in the academy.
        You tell the one Gothon joke you know:
        Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr
        The Gothon stops,tries not to laugh, then busts out laughing and can't move.
        While he's laughing you run up and shoot him squrare in the head
        putting him down, then jump through the Weapon Armory door.'''
        return "laser_weapon_armory"
    else:
        print "DOES NOT COMPUTE"
        return 'central_corridor'
def laser_weapon_armory():
    '''You do a dive roll into the Weapon Armory,crouch and scan the room
    for more Gothons that might be hiding. It's dead quite, too quite.
    You stand up and run to the far side of the room and find the 
    neutron bomb in its container. There's a keypad lock on the box
    and you need the code to get the bomb out. If you get the code
    wrong 10 times then the lock closes forever and you can't
    get the bomb. The code is 3 digits.'''
    code = "%d%d%d" % (randint(1,9), randint(1,9),randint(1,9))
    guess = raw_input("[keypad]>")
    guesses = 0
    while guess != code and guesses <10 :
        print "BZZZZEDDD"
        guesses += 1
        guess = raw_input("[keypad]>")
    if guess == code :
        '''The container clicks open and the seal breaks,letting gas out. 
        You grab the neutron bomb and run as fast as you can th the 
        bridge where you must place it in the right spot .'''
        return 'the_bridge'
    else:
        '''The lock buzzes one last time and you hear a sickening
        melting sound as the mechanism is fused together.
        You decide to sit there, and finally the Gothons blow up the 
        ship from their ship and you die.'''
        return 'death'
def the_bridge():
    '''You burst onto the Bridge with the neutorn destruct bomb
    under your arm and surprise 5 Gothons who are trying to 
    take control of your ship. Each of them has an even uglier
    clown costume than the last. They haven't pulled their
    weapons out yet, as they see the active bomb under your
    arm and don't want to set it off.'''
    action = raw_input(">")
    if action == "throw the bomb":
        print "In a panic you throw the bomb at the group of Gothons "
        print "and make a leap for the door. Right as you drop it a "
        print "Gothon shoots you right in the black killing you."
        print "As you die you see another Gothon frantically try to disarm"
        print "the bomb. You die knowing they will probably blow up when"
        print "it goes off"
        return 'death'
    elif action == "slowly place the bomb":
        print "You point your blaster at the bomb under your arm"
        print "and the Gothon put their hands up and start to sweat"
        print "You inch backward to the door, open it and then carefully"
        print "place the bomb on the floor,pointing your blaster at it"
        print "You then jump back through the door.punch the close button"
        print "and blast the lock so the Gothon can't get out"
        print "Now that the bomb is placed you run to the escape pod to"
        print "get off this tin can"
        return 'escape_pod'
    else:
        print "DOES NOT COMPUTE"
        return "the_bridge"
def escape_pod():
    print "You rush through the ship desperstely trying to make it to"
    print "the eacape pod before the whole ship explodes .It seems like"
    print "hardly any Gothons are on the ship,so your run is clear of "
    print "interference. You get to the chamber with the escape pods, and"
    print "now need to pick one to take. Some of them could be damaged"
    print "but you don't have time to look. There's 5 pods.which one"
    print "do you take?"
    good_pod = randint(1,5)
    guess = raw_input("[pod #]")
    if int(guess) != good_pod:
        print "You jump into pod %s and hit the eject button."%guess
        print "The pod escapes out into the void of space,then"
        print "implodes as the hull ruptures, crushing your body"
        print "into jam jelly"
        return 'death'
    else:
        print "You jump into pod %s and hit the eject button."%guess
        print "The pod easily slides out into space heading to"
        print "the planrt blow. As it flies to the planet.you look"
        print "back and see your ship implode then explode like a"
        print "bright star,taking out the Gothon ship at the same"
        print "time .You won!"
        exit(0)
ROOMS = {'death':death,'central_corridor':central_corridor,'laser_weapon_armory': laser_weapon_armory,'the_bridge': the_bridge,'escape_pod': escape_pod}
def runner(map, start):
    next = start
    while True:
        room = map[next]
        print "\n----------"
        next = room()
runner(ROOMS,'central_corridor')

