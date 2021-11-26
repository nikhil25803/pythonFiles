# Question 1
'''
Write a program to find the frequency of acharacter
in a given string.

char=input()
fre=input()
count=0
for i in range(len(char)):
    if char[i]==str(fre):
        count+=1
print("Frequency of char {} in string {} is {}".format(fre,char,count))
'''

# Question 2
'''
Write a program to print no of vowels, consonant, 
digits and white spaces in a string


string=input()

countVowels=0
countConsonant=0
# countDigits=0 Vowels + Consonants are no of digits
countWS=len(string.split())-1 

vowels=['a','e','i','o','u']


for i in range(len(string)):
    if string[i] in vowels:
        countVowels+=1

    elif string[i] not in vowels:
        countConsonant+=1

    

print("White spaces: ",countWS)
# print(len(string)-1)
print("Consonants are: ",countConsonant-countWS)
print("Vowels are: ",countVowels)
print("Letters are:",countVowels+countConsonant-countWS)
'''
#Question 3 {UNSOLVED}
'''
Write a program to remove all special character 
from a string except alphabets


# Method 1 [Using isalpha()/isnumeric()]
import re

string=input()
values=[char for char in string if char.isalpha() or char.isnumeric()]

result="".join(values)
print(result)


# Method 2 using re modules

import re

string=input()

result=re.sub('[\W_]+','',string)

print(result)
'''

# Question 5
'''
Write a program to concatenate two string
entered by the user


name=input("Enter your name: ")
age=int(input("Enter your age: "))

print("The name os the candidate is",name," and the age is ",age)
'''

# Question 6
''' 
Write a program to check if a string is Palindrome
or not


string=input()
str_rev=string[::-1]
if string==str_rev:
    print("Yes the string is palindrome")
else:
    print("No the string is not Palindrome")
'''

# Question 7

''' 
Write a program to find number of words 
in a statement given by an user

n=input("Enter the statement: ")
count=len(n.split())
print(count)
'''

# Question 8
''' 
Write a program to capitalize first word of
all the words seperated by an user


#Using title method [-Case Sensitive-]
n=input("Enter the statement: ")

result=n.title()
print(result)


#Using Capword method [-Also Case Sensitive-]

import string

n=input("Enter the statement: ")
result=string.capwords(n)

print(result)

# Not a case sensitive method
import  re

word=input()

def convert_to_uppercase(m):
    return m.group(1) + m.group(2).upper()

result=re.sub("(^|\s)(\S)",convert_to_uppercase,word)

print(result)
'''


# Question 9 [-Time Complexity Question-]
''' 
Write a program to find the longest word in a statement
'''
