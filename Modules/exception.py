a=5
b=2

k=int(input("Enter a number: "))
print(k)

try:
    print("Resource Open")
    print(a/b)
    k=int(input("Enter a number: "))
    print(k)

except Exception as e:
    print("You Can not divide a number by Zero:",e)
    


finally:
    print("Resource Closed")

print("Bye !")