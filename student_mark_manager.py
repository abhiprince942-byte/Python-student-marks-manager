# STUDENT MARKSHEET MANAGER
# Group Project
# Members:
# Abhishek Kumar
# Surya Prajapat
# Suraj Kumar
# Arpit Yadav

subjects = ("English", "Maths", "Physics", "Chemistry", "Computer")
students = {}
roll_numbers = set()
# Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    if roll in roll_numbers:
        print("Roll number already exists!")
        return
    name = input("Enter Student Name: ")
    marks = []
    for subject in subjects:
        mark = int(input("Enter marks in " + subject + ": "))
        while mark < 0 or mark > 100:
            print("Enter marks between 0 and 100")
            mark = int(input("Enter marks again: "))
        marks.append(mark)
    students[roll] = [name, marks]
    roll_numbers.add(roll)
    print("Student added successfully!")
# Function to calculate total
def calculate_total(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total
# Function to calculate grade
def calculate_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"
