# Import modules --> library
# Var starts with a letter, then it can have no.s or underscores
# 5 main Data Types: Numbers, Strings, Lists, Tuples, Dictionaries/Maps
# 7 Arithmetic Ops : + , - , * , / , %(remainder) , **(exp) , //(floor divn, ignore remiander & rotate down 14.5 -> 14)
# order of arithmetic op : Multipln &divn b4 addn & subtrn

import random
import sys
import os

print("Hello World")
print('Hello World Again!')
# Comment
'''
Multi-line Comment
This is how it's done!
'''

name = "Kiran"
name_2 = 'Suki'
print(name)
print(name_2)

print("5+2=",5+2)
print("5-2=",5-2)
print("5*2=",5*2)
print("5/2=",5/2)
print("5%2=",5%2)
print("5**2=",5**2)
print("5//2=",5//2)

quote = "\" Always remember you are unique"
multi_line_quote = ''' just
like everyone else'''

quote_all = quote+multi_line_quote
print(quote_all)
print("%s %s %s"%('I like the quote',quote,multi_line_quote))
print('\n'*2)
print("I don't like", end="")
print(" newlines")



