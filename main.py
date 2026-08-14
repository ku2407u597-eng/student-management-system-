# Student Management System

student_name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))

print("\n--- Student Result ---")
print("Student Name:", student_name)
print("Marks:", marks)

if marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")
