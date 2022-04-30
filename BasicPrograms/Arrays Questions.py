from array import*
# Question 1
'''
Write a program to take N elements from user,
stores data and N is the float specialised by the user
Store  data in an array and calculate 
average of those numbers


def avgerage(arr,n):
    avg=0
    for i in range(n):
        avg=avg+arr[i]
        c=avg/n
    return c

len=int(input("Enter the length: "))
arr=[int(i) for i in input().split()]
print(avgerage(arr,len))
'''

#Question 2
'''
Write a program to take n inputs from
the user and display the largest value


def largest(arr):
    return max(arr)

n=int(input("Enter the length of the input: "))
arr=[int(i) for i in input().split()]
print(arr)
print(largest(arr))
'''

# Question 3
'''
Write a program to find the Standard deviation of
N inputs given by the user stored in an array
'''