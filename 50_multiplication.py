#Print the Multiplication Table of a Given Number

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
