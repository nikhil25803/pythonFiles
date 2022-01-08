a=[1,5,88,98,3]
a[2]=67 #used to change the value of list
print(a)


#list of can be created of diffrent types

c=[45, "Nikhil", False, 45.56]
print(c)

#list SLicing
friends=["Nikhil", "Rohan", "Rakul", 45]
print(friends[1:3])

#List Indexing and METHODS
l1=[1,5,4,21,78,15]
print(l1)

l1.sort()
print(l1)   #print list in accending order

l1.reverse()  # it reverse the order of list
print(l1)

l1.append(8) # it add that particular element in the list but at last
print(l1)

l1.append(9)  # arranged list in accending order after adding the new element
l1.sort()
print(l1)


l1.insert(1,78)
print(l1)  #This will add 78 at first position

l1.remove(21)
print(l1)  #Remove the exact valued 21 element from the list

l1.pop(2)
print(l1) #This will delete element at index 2





























