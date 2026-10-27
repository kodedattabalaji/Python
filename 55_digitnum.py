#Find the Sum of the Digits of a Number

n = int(input("Enter a number: "))
n = abs(n)
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum of digits =", total)
