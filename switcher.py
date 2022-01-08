def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def default(a,b):
    return "Invalid Input"

switcher={
    1: add,
    2: sub,
    3: mul,
    4: div,
}


def switch(op,a,b):
    return switcher.get(op,default)(a,b)


print('''Enter your preference: 
1. Addition
2. Subtraction
3. Multiply
4. Division
''')


choice=int(input("Enter your choice: "))
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

print(switch(choice,a,b))




















