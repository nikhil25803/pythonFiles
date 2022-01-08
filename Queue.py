l=[]

while True:
    c=int(input('''
    1 Push
    2 Pop
    3 Front
    4 Last
    5 Display
    6 Exit
    
    '''))

    if c==1:
        n=input("Enter the value: ")
        l.append(n)
        print(l)
    
    elif c==2:
        if len(l)==0:
            print("Empty List")
        else:

            del l[0]
            
            print(l)

    else:
        break

    