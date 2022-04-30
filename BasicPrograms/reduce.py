from functools import *

# def add(a,b):
#     return a+b


num=[3,2,4,5,6,7,8,9,10]


evens=list(filter(lambda n:n%2==0,num)) #Filtered Value

even_2=list(map(lambda x: x*2,evens)) #Operation on Filtered Value

sums=reduce(lambda x,y:x*y,even_2) # Furthur Operation

print(sums)