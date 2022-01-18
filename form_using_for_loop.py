for i in range(1,4):
    person=input("Enter your name: ")
    with open(f"details/Person{person}.txt",'w') as f:
        branch=input("Enter your Branch: ")
        age=int(input("Enter your age: "))
        roll=int(input("Enter your roll number: "))
        f.write(f"Hello! My name is {branch}\nI am {age}\nand my roll number is {roll}")