a={1,3,4,5,1}
print(a)  # repetetive elements are not printed
print(type(a))


b={}
print(type(b)) #this is an emept dict not set


#for empty set use

c=set()
print(type(c))  #this will print an empty set


#Methods in a set

d=set()
d.add(5)
d.add(2)
d.add(3)

d.add(8) # adding a value repetedily doesnt change the value
print(d)
print(len(d))  #Print the length of the set (tuple will be considered as an element)

#List and Dictionary can not be added but tupples can
d.add((7,8,9))
print(d)


#Operators in set

s={1,8,9,56,89,54,54}
print(len(s)) #print the length of this set

s.remove(1)
print(s) #remove a value

print(s.pop())

print(s)




















