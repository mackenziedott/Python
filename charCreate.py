# -*- coding: utf-8 -*-
"""
Created on Mon May 01 19:17:55 2017

@author: Mackenzie
"""

def charCreate():
    classlist = ["Bard", "Fighter", "Wizard", "Druid", "Barbarian", "Cleric", "Warlock", "Sorceror", "Rogue", "Ranger", "Paladin"]
    classIntrostring = '''
    What class does your character want to be? Enter the following to select your class:
    1: Bard
    2: Fighter
    3: Wizard
    4: Druid
    5: Barbarian
    6: Cleric
    7: Warlock
    8: Sorceror
    9: Rogue
    10: Ranger
    11: Paladin
    '''
    racelist = ["Human", "Human (Variant)", "Elf", "Half-Elf", "Half-Orc", "Dwarf", "Gnome", "Halfling", "Tiefling", "Dragonborn"]
    raceIntroString = '''
    What Race does your character want to be? Enter the following to select your race:
    1: Human
    2: Human (variant)
    3: Elf
    4: Half-Elf
    5: Half-Orc
    6: Dwarf
    7: Gnome
    8: Halfling
    9: Tiefling
    10: Dragonborn
    '''
    statDistributionString = '''
    
    1: Strength
    2: Dexterity
    3: Constitution
    4: Intelligence
    5: Wisdom
    6: Charisma
    '''
    fixedstatDistributionString = textwrap.dedent(statDistributionString).strip()
    fixedraceIntroString = textwrap.dedent(fixedraceIntroString).strip()
    StatList = [0,0,0,0,0,0]
    fixedClassIntrostring = textwrap.dedent(classIntrostring).strip()
    print  fixedClassIntrostring
    
    print("Time to make your character\n")
    print("First step is Stat Distribution using standard distribution\n")
    print(fixedstatDistributionString)
    selstat1 = input("What stat do you want 15 in: ")
    selstat1int = int(selsat1)
    selstat2 = input("What stat do you want 14 in: ")
    selstat2int = int(selsat2)
    selstat3 = input("What stat do you want 13 in: ")
    selstat3int = int(selsat3)
    selstat4 = input("What stat do you want 12 in: ")
    selstat4int = int(selsat4)
    selstat5 = input("What stat do you want 10 in: ")
    selstat5int = int(selsat5)
    selstat6 = input("What stat do you want 8 in: ")
    selstat6int = int(selsat6)
    StatList(selstat1int) = 15
    StatList(selstat2int) = 14
    StatList(selstat3int) = 13
    StatList(selstat4int) = 12
    StatList(selstat5int) = 10
    StatList(selstat6int) = 8
    #Class Selction
    print(classIntrostring)
    selclass = input("Enter what class you want: ")
    selclassint = int(selclass)
    dclass = classlist(selclassint)
    #Race Selction
    print(raceIntroString)
    selrace = input("Enter what Race you want: ")
    selraceint = int(selrace)
    name = input("what is your character's name? ")
    drace = racelist(selraceint)
    data = StatList.append([dclass, drace, name])
    return [data]
    