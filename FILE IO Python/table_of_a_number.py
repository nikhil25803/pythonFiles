# Taking the number as a user input
num = int(input("Enter the number: "))


with open("table.txt","w") as f:

    # using loop for multiplication
    for i in range(1,11):

        # f string method us used to print variables
        f.write(f"{num} X {i} = {num*i}\n")