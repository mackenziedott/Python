# -*- coding: utf-8 -*-
"""
Created on Sat Jul 01 10:53:08 2017

@author: Mackenzie
"""
hourlist = ['twelve', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven']
minute10list =['o', 'teen', 'twenty', 'thirty', 'fourty', 'fifty'] 
minutelist = ['', 'one', ' two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teenlist = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
print "Welcome to the talking clock. The input format is hh:mm"
clockinput = ''
while clockinput != "!q":
    clockinput = raw_input("\n Enter Time here: ")
    #convert into hour
    hour = clockinput[0:2]
    tenminute = clockinput[3:4]
    minute = clockinput[4:5]
    inthour = int(hour)
    intminute = int(minute)
    inttenminute = int(tenminute)
    #print inthour
    #print intminute
    
    #output
    #Hour Conversion
    if inthour >= 12:
        inthour = inthour - 12
        ending = 'pm'
    else:
        ending = 'am'
    hourstring = hourlist[inthour]
    #10inute conversion
    if inttenminute == 1:
        tenminutestring = ''
        minutestring = teenlist[intminute]
    else:
        tenminutestring = minute10list[inttenminute]
        minutestring = minutelist[intminute]
    print "It's",hourstring, tenminutestring, minutestring, ending