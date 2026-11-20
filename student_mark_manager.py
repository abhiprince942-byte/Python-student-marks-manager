# Python-student-marks-manager
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


# Function to display marksheet

def display_marksheet():

    if students == []:

        print("No student records found!")

        return

    print("\n========== CLASS MARKSHEET ==========")

    for student in students:

        roll = student[0]

        name = student[1]

        marks = student[2]

        total = calculate_total(marks)

        percentage = total / 5

        grade = calculate_grade(percentage)

        print("\nRoll Number:", roll)

        print("Name:", name)

        for i in range(5):

            print(subjects[i], ":", marks[i])

        print("Total Marks:", total, "/ 500")

        print("Percentage:",percentage,"%")

        print("Grade:",grade)


     
 # Function to find class topper
def class_statistics():

    if students == []:
        print("No student records found!")
        return

    highest = -1
    topper = ""
    total_percentage = 0
    count = 0

    subject_total = [0, 0, 0, 0, 0]

    for student in students:

        marks = student[2]

        total = calculate_total(marks)
        percentage = total / 5

        total_percentage = total_percentage + percentage
        count = count + 1

        if total > highest:
            highest = total
            topper = student[1]

        for i in range(5):
            subject_total[i] = subject_total[i] + marks[i]

    print("\n========== CLASS STATISTICS ==========")

    print("Class Topper:", topper)
    print("Topper Marks:", highest)
    print("Class Average:", total_percentage / count, "%")

    print("\nSubject Wise Average:")

    for i in range(5):
        print(subjects[i], ":", subject_total[i] / count)

# Function to search student

def search_student():

    name = input("Enter student name: ")

    found = False

    for student in students:

        if student[1].lower() == name.lower():

            print("\nStudent Found!")

            print("Roll Number:", student[0])

            print("Name:", student[1])

            total = calculate_total(student[2])

            percentage = total / 5

            print("Total Marks:", total)

            print("Percentage:", percentage, "%")

            print("Grade:", calculate_grade(percentage))

            found = True

    if found == False:

        print("Student not found!")



# Main Menu
while True:

    print("\n================================")
    print("    STUDENT MARKSHEET MANAGER")
    print("================================")

    print("1. Add Student")
    print("2. Display Marksheet")
    print("3. Class Statistics")
    print("4. Search Student")
    print("5. Exit")

    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_marksheet()

    elif choice == "3":
        class_statistics()

    elif choice == "4":
        search_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")




















































