# A function that calls itself

# n!=1*2*3*4.....(n-1)*n
'''
n=int(input(55))
pr=1
for i in range(n):
    pr=pr*(i+1)
print(pr)
'''
# Using defined function
'''
def factorial_iter(n):
    pr=1
    for i in range(n):
        pr=pr*(i+1)
    return pr
f=factorial_iter(5)
print(f)
'''

# Using recursion

def fact_recursive(n):
    if n==1 or n==0:
        return 1 
    return n*fact_recursive(n-1)

f=fact_recursive(5)
print(f)