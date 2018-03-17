import random
import sys
import os

'''Conditional Statements -----------------
if else elif == != > >= <= and or not
white space used to group blocks of code
-------------------------------------------'''
age = 30

if age >= 21:
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive a car')
else:
    print('You are not old enough to drive')

if ((age>=1) and (age <= 18)):
    print('You get a birthday')
elif((age == 21) or (age >= 65)):
    print("You get a birthday")
elif not(age == 30):
    print("You don't get a party :( ")
else:
    print('You get a birthday party yeah :) ')
print('\n'*0)

''' Loop for 10 times: ----------------------
perform action from 0 to 10 but not 10-------'''

for x in range(0,10):
    print(x,' ', end="")
print('\n')

grocery_list = ['Juice','Tomatoes','Potatoes','Bananas']
for y in grocery_list:
    print(y)

for x in [1,3,5,7,9]:
    print(x)

print('\n')
num_list = [[1,2,3],[10,20,30],[100,200,330]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

print('\n')
random_num = random.randrange(0,20)
while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0, 20)

print('\n')
i=0
while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 11):
        break
    else:
        i += 1 # i=i+1
        continue #Skip all from this in while loop, goto begin

    i += 1






