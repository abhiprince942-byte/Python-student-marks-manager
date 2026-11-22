# Python Student Marks Manager

A simple menu-driven Python project designed to manage student records, calculate marks, generate marksheets, and analyze class performance.

## Project Description

The **Student Marks Manager** is a Python-based group project that allows users to add student details, enter subject-wise marks, generate individual marksheets, search for students, and view class statistics.

This project is developed using basic Python programming concepts such as lists, tuples, loops, conditional statements, and functions.

## Features

- **Add Student:** Enter student roll number, name, and subject-wise marks.
- **Duplicate Roll Number Check:** Prevents adding students with an existing roll number.
- **Marks Validation:** Accepts marks only between 0 and 100.
- **Display Marksheet:** Displays individual student details and subject-wise marks.
- **Total Marks Calculation:** Calculates total marks out of 500.
- **Percentage Calculation:** Calculates the student's overall percentage.
- **Grade Calculation:** Assigns grades according to the percentage.
- **Class Statistics:** Displays the class topper and overall class average.
- **Subject-wise Average:** Calculates average marks in each subject.
- **Search Student:** Finds a student using their roll number.

## Subjects

The project includes five subjects:

1. English
2. Maths
3. Physics
4. Chemistry
5. Computer

Each subject carries 100 marks, making the maximum total **500 marks**.

## Grading System

| Percentage | Grade |
|---|---|
| 80% and above | A |
| 60% – 79% | B |
| 40% – 59% | C |
| Below 40% | Fail |

## Technologies and Concepts Used

**Technology:**
- Python 3
- Visual Studio Code
- GitHub

**Python Concepts:**
- Variables and Data Types
- Lists and Nested Lists
- Tuples
- For and While Loops
- Conditional Statements (if, elif, else)
- Functions
- User Input and Output

## Project Structure

```text
Python-student-marks-manager/
│
├── student_mark_manager.py
│
└── README.md
```

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/abhiprince942-byte/Python-student-marks-manager.git
```

### Step 2: Open the Project Folder

```bash
cd Python-student-marks-manager
```

### Step 3: Run the Python Program

```bash
python student_mark_manager.py
```

## Main Menu

When you run the program, the following menu appears:

```text
================================
    STUDENT MARKSHEET MANAGER
================================
1. Add Student
2. Display Marksheet
3. Class Statistics
4. Search Student
5. Exit
================================
Enter your choice:
```

Choose an option from the menu to perform the required operation.

## How It Works

1. Select the **Add Student** option.
2. Enter the student's roll number and name.
3. Enter marks in all five subjects.
4. Select **Display Marksheet** to view student results.
5. Select **Class Statistics** to view the class topper and class performance.
6. Use **Search Student** to find a particular student's result.
7. Select **Exit** to close the program.

**Note:** Student records are stored in memory during program execution. They are not permanently saved after the program exits.

## Group Members

1. Abhishek Kumar
2. Surya Prajapat
3. Suraj Kumar
4. Arpit Yadav

## Future Improvements


- Add options to update and delete student records.
- Improve the user interface.
- Add more student performance reports.

---

**Project Name:** Python Student Marks Manager  
**Programming Language:** Python 3  
**Project Type:** Group Project
