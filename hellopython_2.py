import random
import sys
import os

grocery_list = ['Juice','Tomatoes','Potatoes',
                'Bananas']
print('First Item is',grocery_list[0])

grocery_list[0]="Green Juice"
print('First Item is',grocery_list[0])

print('\n',grocery_list[1:3])

other_events = ['Wash Car','Pick up Kids','Cash Check']

to_do_list = [other_events,grocery_list]
print('\n'*1,to_do_list)
print('\n'*0)
print((to_do_list[1][1]))
grocery_list.append('Onions')
print(to_do_list)
grocery_list.insert(1,"Pickle")
grocery_list.remove("Pickle")
grocery_list.sort()
grocery_list.reverse()
del grocery_list[4]
print(to_do_list)

to_do_list_2 = other_events+grocery_list
print(to_do_list_2)
print(len(to_do_list_2))
print("Max is",max(to_do_list_2))
print("Min is",min(to_do_list_2))
