l=[]

while True:
    c=int(input('''
    1 Push
    2 Pop
    3 Peek
    4 Display
    5 Exit
    
    '''))

    if c==1:
        n=input("Enter the value: ")
        l.append(n)
        print(l)
    
    elif c==2:
        if len(l)==0:
            print("Empty List")
        else:

            p=l.pop()
            print(p)
            print(l)

    else:
        break

    