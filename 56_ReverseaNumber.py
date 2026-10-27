#Reverse a Number

n = int(input("Enter a number: "))
num = abs(n)
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if n < 0:
    rev = -rev

print("Reversed number =", rev)
