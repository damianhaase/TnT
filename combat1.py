#! /usr/bin/env python

# this is my first attempt at a python module that will simulate a combat
# round in TnT

# now i need to have it do multiple rounds of combat, keep track of hit points, and report who won

import dice_roller # this is for dice rolling


# character stats for simple combat - deprecated
######################################

# char1_name = 'Barry'
# char1_persAdds = 4
# char1_weapon = 'Sabre'
# char1_weaponDice = 3
# char1_weaponAdds = 4
# char1_CN = 18

# char2_name = 'Manticore'
# char2_MR = 16
# char2_weaponDice = round(char2_MR / 10, 0) + 1
# char2_weaponAdds = round(char2_MR / 2, 0)

######################################


# set up characters - new version
######################################

# list of attributes:
# name str
# weapon str
# weapon_dice int
# weapon adds int
# personal adds
# CN int

# character stats are dictonarys
char1 = { 'name' : 'Barry', 'weapon' : 'Sabre', 'weapon_dice' : 3, 'weapon_adds' : 4, 'personal_adds': 4, 'CN' : 18 };
char2 = { 'name' : 'Manticore', 'weapon' : 'Claws', 'weapon_dice' : 4, 'weapon_adds' : 0, 'personal_adds': 15, 'CN' : 30 };
char3 = { 'name' : 'Six Pack', 'weapon' : 'Fists', 'weapon_dice' : 3, 'weapon_adds' : 0, 'personal_adds': 4, 'CN' : 24 };

# charlist is a list containing each character dictionary
charList = [char1, char2, char3];

print ""
print "Set sides. There are %d characters to allocate." % len(charList)
print "1: %s, %d personal adds, using %s, %dd6+%d, %d CN" % ( char1['name'], char1['personal_adds'], char1['weapon'], char1['weapon_dice'], char1['weapon_adds'], char1['CN'] )
print "2: %s, %d personal adds, using %s, %dd6+%d, %d CN" % ( char2['name'], char2['personal_adds'], char2['weapon'], char2['weapon_dice'], char2['weapon_adds'], char2['CN'] )
print "3: %s, %d personal adds, using %s, %dd6+%d, %d CN" % ( char3['name'], char3['personal_adds'], char3['weapon'], char3['weapon_dice'], char3['weapon_adds'], char3['CN'] )
print ""

# set up sides in battle
######################################

# set a variable to determine if each side has at least one character
nonZeroSides = 0

# do this loop until nonZeroSides is 1
while nonZeroSides == 0:
    # initialize the side lists
    # each side is a list, which gets the the full dictionary for each char added
    aSide = [];
    bSide = [];
    for ch in charList:
        currentName = ch['name'];
        char1_sideinput = raw_input ("%s, side a or b? " % currentName)
        if (char1_sideinput == 'a'):
            aSide.append ( ch ); 
        elif (char1_sideinput == 'b'):
            bSide.append ( ch ); 

    # check number of characters in sides
    if len(aSide) == 0 or len(bSide) == 0:
        print ""
        print "need at least one character per side!"
        print "let's try again."
        print ""
    elif len(aSide) >= 1 and len(bSide) >=1:
        nonZeroSides = 1

print ""
print "The sides as they stand:"
print ""
# run a loop through each Side list, listing the names from each dictionary
# at the same time, add the key HP and assign it the value from CN
print "Side a: %d characters" % len(aSide)
for ch in aSide:
   print "  %s" % ch['name']
   ch.update({"HP" : ch['CN']})
print ""
print "Side b: %d characters" % len(bSide)
for ch in bSide:
   print "  %s" % ch['name']
   ch.update({"HP" : ch['CN']})
print ""

# now we know how many characters will be one each side. 
# and we have a working HP number
# next, we have each character roll and add the results up per side

# one round first
aSideRollTotal = 0
for ch in aSide:
    roll = dice_roller.multiDie( ch['weapon_dice'] , 1 )
    print "  %s rolls %d + %d adds" % (ch['name'], roll, ch['weapon_adds'] + ch['personal_adds'])
    aSideRollTotal = aSideRollTotal + roll + ch['weapon_adds'] + ch['personal_adds']
print "  %d total for Side a" % aSideRollTotal
print ""

bSideRollTotal = 0
for ch in bSide:
    roll = dice_roller.multiDie( ch['weapon_dice'] , 1 )
    print "  %s rolls %d + %d adds" % (ch['name'], roll, ch['weapon_adds'] + ch['personal_adds'])
    bSideRollTotal = bSideRollTotal + roll + ch['weapon_adds'] + ch['personal_adds']
print "  %d total for Side b" % bSideRollTotal
print ""

# then we determine how to assign the damage
if aSideRollTotal == bSideRollTotal:
    print "It's a draw"
elif aSideRollTotal > bSideRollTotal:
    hitsToAllocate = aSideRollTotal - bSideRollTotal
    print "Side a gets %d hits on Side b." % hitsToAllocate
elif aSideRollTotal < bSideRollTotal:
    hitsToAllocate = bSideRollTotal - aSideRollTotal
    print "Side b gets %d hits on Side a."  % hitsToAllocate
    

# then we decide if we want to do another combat round



######################################



# combat results display
######################################

# while either character's HP > 0, run the combat round loop
# round = 1
# while (char1_HP > 0  and char2_HP > 0):
#     char1_roll = dice_roller.multiDie( char1_weaponDice , 1 )
#     char1_total = char1_roll + char1_weaponAdds
#     char2_roll = dice_roller.multiDie( char2_weaponDice , 1 )
#     char2_total = char2_roll + char2_weaponAdds
#    print "%s rolled %d: %d + %d adds" % (char1_name , char1_roll + char1_weaponAdds, char1_roll, char1_weaponAdds)
#    print "%s rolled %d: %d + %d adds" % (char2_name , char2_roll + char2_weaponAdds, char2_roll, char2_weaponAdds)
    
#     if char1_total == char2_total: 
#         print "%d    draw" % round
#     elif char1_total > char2_total:
#         char2_HP = char2_HP - (char1_total - char2_total)
#         if (char2_HP <= 0):
#             print "%d    %s is dead" % (round, char2_name)
#             break
#         print "%d    %s %d" % (round, char2_name, char2_HP)
#     elif char1_total < char2_total:
#         char1_HP = char1_HP - (char2_total - char1_total)
#         if (char1_HP <= 0):
#             print "%d    %s is dead" % (round, char1_name)
#             break
#         print "%d    %s %d" % (round, char1_name, char1_HP)
#     round = round + 1
######################################
