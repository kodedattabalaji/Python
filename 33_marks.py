#Display Grades Based on Marks
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
elif marks >= 0:
    print("Fail")
else:
    print("Invalid marks")