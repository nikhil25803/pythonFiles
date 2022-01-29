
for i in range(1,16):

    with open(f"tables/Multiplication_Of_{i}.txt","w") as f:

        for j in range(1,11):

            f.write(f"{i} X {j} = {i*j}\n")