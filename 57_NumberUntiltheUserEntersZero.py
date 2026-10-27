#Number Until the User Enters Zero

while True:
    n = int(input("Enter a number (0 to stop): "))

    if n == 0:
        print("Program stopped.")
        break

    print("You entered:", n)
