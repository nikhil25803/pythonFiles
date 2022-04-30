# def is_even(n):
#     return n%2==0


# Using Lambda



num=[3,2,4,5,6,7,8,9,10]

evens=list(filter(lambda n: n%2==0,num))

print(evens)