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


# set up sides
######################################

# list of attributes:
# name str
# weapon str
# weapon_dice int
# weapon adds int
# personal adds
# CN int


char1 = { 'name' : 'Barry', 'weapon' : 'Sabre', 'weapon_dice' : 3, 'weapon_adds' : 4, 'personal_adds': 4, 'CN' : 18 };
char2 = { 'name' : 'Manticore', 'weapon' : 'Claws', 'weapon_dice' : 2, 'weapon_adds' : 0, 'personal_adds': 8, 'CN' : 18 };
char3 = { 'name' : 'Six Pack', 'weapon' : 'Fists', 'weapon_dice' : 3, 'weapon_adds' : 0, 'personal_adds': 4, 'CN' : 24 };

charList = [char1, char2, char3];

print "Set sides. There are %d characters to allocate." % len(charList)

print "1: %s, %d personal adds, using %s, %dd6+%d, %d CN" % ( char1['name'], char1['personal_adds'], char1['weapon'], char1['weapon_dice'], char1['weapon_adds'], char1['CN'] )
print "2: %s, %d personal adds, using %s, %dd6+%d, %d CN" % ( char2['name'], char2['personal_adds'], char2['weapon'], char2['weapon_dice'], char2['weapon_adds'], char2['CN'] )
print "3: %s, %d personal adds, using %s, %dd6+%d, %d CN" % ( char3['name'], char3['personal_adds'], char3['weapon'], char3['weapon_dice'], char3['weapon_adds'], char3['CN'] )

# make some sides
aSide = [];
bSide = [];

for character in charList:
    currentName = character['name'];
    char1_sideinput = raw_input ("%s, side a or b? " % currentName)
    if (char1_sideinput == 'a'):
        aSide.append ( currentName ); 
    elif (char1_sideinput == 'b'):
        bSide.append ( currentName ); 
print "the sides as they stand:"
print "side a: %s" % aSide;
print "side b: %s" % bSide;

######################################



# combat results display
######################################

print "This will simulate multiple combat rounds between the following characters:"
print "%s, Human, %d personal adds, %d HP, using %s %dD6+%d" % (char1_name, char1_persAdds, char1_CN, char1_weapon, char1_weaponDice, char1_weaponAdds)
print "vs."
print "%s, MR %d, %dD6+%d, %d HP" % (char2_name, char2_MR, char2_weaponDice, char2_weaponAdds, char2_MR)

# make copies of CN and MR to decrement
char1_HP = char1_CN
char2_HP = char2_MR

# while either character's HP > 0, run the combat round loop
round = 1
while (char1_HP > 0  and char2_HP > 0):
    char1_roll = dice_roller.multiDie( char1_weaponDice , 1 )
    char1_total = char1_roll + char1_weaponAdds
    char2_roll = dice_roller.multiDie( char2_weaponDice , 1 )
    char2_total = char2_roll + char2_weaponAdds
    #print "%s rolled %d + %d adds" % (char1_name , char1_roll, char1_weaponAdds)
    #print "%s rolled %d + %d adds" % (char2_name , char2_roll, char2_weaponAdds)
    
    if char1_total == char2_total:
        print "%d    draw" % round
    elif char1_total > char2_total:
        char2_HP = char2_HP - (char1_total - char2_total)
        if (char2_HP <= 0):
            print "%d    %s is dead" % (round, char2_name)
            break
        print "%d    %s %d" % (round, char2_name, char2_HP)
    elif char1_total < char2_total:
        char1_HP = char1_HP - (char2_total - char1_total)
        if (char1_HP <= 0):
            print "%d    %s is dead" % (round, char1_name)
            break
        print "%d    %s %d" % (round, char1_name, char1_HP)
    round = round + 1
######################################
