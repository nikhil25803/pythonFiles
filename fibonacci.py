# Iterative approach

def febiter(n):
    a=0
    b=1
    for i in range(1,n):
        c=a
        a=b
        b=a+c
    return b





# Recursive approach 

def fibrecur(n):
    fib=[0,1]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        
        return fibrecur(n-1)+fibrecur(n-2)


num=int(input())
print(febiter(num))
