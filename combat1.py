#! /usr/bin/env python

# this is my first attempt at a python module that will simulate a combat
# round in TnT

import dice_roller # this is for dice rolling

char1_name = 'Barry'
char1_persAdds = 4
char1_weapon = 'Sabre'
char1_weaponDice = 3
char1_weaponAdds = 4

char1_roll = dice_roller.multiDie( char1_weaponDice , 1 )
char1_total = char1_roll + char1_weaponAdds

char2_name = 'Manticore'
char2_MR = 25
char2_weaponDice = round(char2_MR / 10, 0) + 1
char2_weaponAdds = round(char2_MR / 2, 0)

char2_roll = dice_roller.multiDie( char2_weaponDice , 1 )
char2_total = char2_roll + char2_weaponAdds


print "This will simulate a combat round between the following characters:"
print "%s, Human, %d personal adds" % (char1_name, char1_persAdds)
print "using %s %dD6+%d" % (char1_weapon, char1_weaponDice, char1_weaponAdds)

print "vs."

print "%s" % char2_name
print "MR %d, %dD6+%d" % (char2_MR, char2_weaponDice, char2_weaponAdds)

print "... dice are rolled!"

print "%s rolled %d + %d adds" % (char1_name , char1_roll, char1_weaponAdds)
print "%s rolled %d + %d adds" % (char2_name , char2_roll, char2_weaponAdds)

if char1_total == char2_total:
    print "This round was a draw."
elif char1_total > char2_total:
    print "%s wins this round, doing %d points of damage to %s" % (char1_name, char1_total - char2_total, char2_name)
elif char1_total < char2_total:
    print "%s wins this round, doing %d points of damage to %s" % (char2_name, char2_total - char1_total, char1_name)
