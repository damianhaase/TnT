#! /usr/bin/env python

# this is my first attempt at a python module that will simulate a combat
# round in TnT

# now i need to have it do multiple rounds of combat, keep track of hit points, and report who won

import dice_roller # this is for dice rolling


# character stats
######################################

char1_name = 'Barry'
char1_persAdds = 4
char1_weapon = 'Sabre'
char1_weaponDice = 3
char1_weaponAdds = 4
char1_CN = 18

char2_name = 'Manticore'
char2_MR = 16
char2_weaponDice = round(char2_MR / 10, 0) + 1
char2_weaponAdds = round(char2_MR / 2, 0)

######################################


# display
######################################

print "This will simulate multiple combat rounds between the following characters:"
print "%s, Human, %d personal adds" % (char1_name, char1_persAdds)
print "%d HP" % char1_CN
print "using %s %dD6+%d" % (char1_weapon, char1_weaponDice, char1_weaponAdds)

print "vs."

print "%s" % char2_name
print "MR %d, %dD6+%d" % (char2_MR, char2_weaponDice, char2_weaponAdds)
print "%d HP" % char2_MR


# make copies of CN and MR to decrement
char1_HP = char1_CN
char2_HP = char2_MR

# while either character's HP > 0, run the combat round loop
round = 1
while (char1_HP > 0  and char2_HP > 0):
    print "Combat round %d:" % round    
    round = round + 1
    char1_roll = dice_roller.multiDie( char1_weaponDice , 1 )
    char1_total = char1_roll + char1_weaponAdds
    char2_roll = dice_roller.multiDie( char2_weaponDice , 1 )
    char2_total = char2_roll + char2_weaponAdds
    #print "%s rolled %d + %d adds" % (char1_name , char1_roll, char1_weaponAdds)
    #print "%s rolled %d + %d adds" % (char2_name , char2_roll, char2_weaponAdds)
    
    if char1_total == char2_total:
        print "This round was a draw."
    elif char1_total > char2_total:
        print "%s wins this round, doing %d points of damage to %s" % (char1_name, char1_total - char2_total, char2_name)
        char2_HP = char2_HP - (char1_total - char2_total)
        print "%s now has %d HP" % (char2_name, char2_HP)
    elif char1_total < char2_total:
        print "%s wins this round, doing %d points of damage to %s" % (char2_name, char2_total - char1_total, char1_name)               
        char1_HP = char1_HP - (char2_total - char1_total)
        print "%s now has %d HP" % (char1_name, char1_HP)
    
if (char1_HP <= 0):
    print "%s is dead" % char1_name
elif (char2_HP <= 0):
    print "%s is dead" % char2_name