n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    print("*"*(i-1),end="")
    print(" "*(n-i))

