import random
import sys
import os

''' Functions-------------
Reuse/readable code
Define function before calling it
Variables defined inside a function has local scope only
--------------------------'''

def Add_Number_Fun(FirstNum, LastNum):
    SumNum = FirstNum + LastNum
    return SumNum

print(Add_Number_Fun(5,4))
temp = Add_Number_Fun(2,3)
print(temp)

'''Input from user---------
---------------------------'''
print('What is your name?')
name = 'suki' #sys.stdin.readline()
print('Hello',name)

'''Strings Detailed---------
concatenate strings by +
.5f - floating point number with 5 dec places
---------------------------'''
long_string = " i'll catch you if you fall - The Floor"
print(long_string[0:7])
#print last 5 characters
print(long_string[-5:]) #Last 5 strings
print(long_string[:-5])#All upto last 5
print(long_string[:4] + " be there")
print("%c is my %s letter and my number %d number is %.5f"
      % ('S','favourite',1,.25))
print(long_string.capitalize())#capitalise 1st letter

print(long_string.find("Floor"))#index of Floor;case sensitive!

print(long_string.isalpha())# are all letters?
print(long_string.isalnum())#are all numbers?
print('\n')
print(len(long_string))
print(long_string.replace('Floor','Ground'))
print(long_string.strip())#strip white space
#to split a string into a list
quote_list = long_string.split(" ")
print(quote_list)



''' File I/O-------------
When opening a new file or existing file, 
mention the mode as read or write or both
wb : write mode
r+ : read & write mode
--------------------------'''
test_file = open("test.txt","wb")
print(test_file.mode)#prints the file mode
print(test_file.name)
#To write test to the file
test_file.write(bytes("Everyday in Every way I'm getting"
                      " Better and Better!\n", 'UTF-8'))
test_file.close()
#since closed, reopen the file
test_file = open("test.txt","r+")
text_in_file = test_file.read()
print(text_in_file)
test_file.close()
#to delete the file(close the file b4 remove)
os.remove("test.txt")





























