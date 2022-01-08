# Map is used to operate on the filtered value

num=[3,2,4,5,6,7,8,9,10]

evens=list(filter(lambda n:n%2==0,num))

# print(evens)

even_2=list(map(lambda x: x*2,evens))

#Reduce



print(even_2)