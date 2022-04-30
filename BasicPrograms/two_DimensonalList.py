row=int(input("Enter the number of rows: "))
col=int(input("Enter the number of coloumn: "))

matrix=[]

for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input()))
    matrix.append(a)


print("Printing the matrix: ")
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()