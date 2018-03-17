import random
import sys
import os

'''TUPLES - When you have data that do not want easily to be changed. 
 To change a tuple convert it to list and change and then back to tuple
 (not done usually)
'''
pi_tuple = (3,1,4,1,5,9,10)

new_list = list(pi_tuple)
new_tuple = tuple(new_list)

print(len(pi_tuple))
print(min(pi_tuple))
print(max(new_tuple))

'''Dictionary/Maps - made up of unique key for each value
(simialr to list, but cant join maps like we do for lists with + sign)
 Use caurly brace for map, Enter key followed by colon and their value'''

# Super heros/villains name and their secret identity

super_villains = {'Fiddler':'Issac Bowin','Captain Cold':'Leonard Snart',
                  'Weather Wizard':'Mark Mardon','Mirror Master':'Sam Scudder',
                  'Pied Piper':'Thomas Peterson','Wonder Woman':'Princess Diana of Themyscira',
                  'Spiderman':'Peter Parker'}
print(super_villains['Wonder Woman'])
del super_villains['Fiddler']
super_villains['Pied Piper'] ='Hartley Rathway'
print(len(super_villains))
print(super_villains.get("Pied Piper"))
print(super_villains.keys())
print(super_villains.values())