# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:06:47 2017

@author: Mackenzie
"""
# DND 5E Character Creator
print "Welcome to Mack's DND 5E Character Creator and Manager"
validmenu = 0
while validmenu == 0:
    print "Enter C to create a new character or R to review an old character or Q to Quit"
    option = input("Enter Choice: ")
    if option == "C":
        validmenu = 1
    elif option == "R":
        validmenu = 2
    elif option == "Q"
        print "goodbye"
        #Enter Quit Command Here
    else:
        print "Answer Not Valid, Try Again"
if validmenu = 1:
    data = charCreate()
    newstatslist = [data(1),data(2),data(3),data(4),data(5),data(6)]
    newdclass = data(7)
    newdrace = data(8)
    newname = data(9)
    newchar = Character(newname,newstatslist,newdclass,newdrace)
    
if validmenu = 2:
    #Load Character Creation File

class Character:
    "Common base class for all characters"
    def __init__(self, name, statslist, dclass, drace):
        self.dclass = dclass
        self.drace = drace
        self.statslist = statslist
        self.name = name
    def displayCharacterRecord:
        print "Name : ", self.name, ", Race: ", self.drace, ", Class: ", self.dclass
        print "\n Strength: ", self.statslist(1)
        