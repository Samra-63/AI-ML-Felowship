# Student Management System (SMS) – Python Project

Hi! My name is Samra and this is my Python project for a basic Student Management System. I made this to practice some important Python concepts like classes (OOP), file reading/writing, creating my own Python package, and also using iterators and generators.

This project helped me understand how a simple system can manage student data like name, ID, courses, grades, attendance, etc.

## Project Files  (What’s Inside)?

### 1. `SMS.py`
In this file, I created two classes:
- `Student` → for storing details like name, age, student ID, and courses.
- `GraduateStudent` → a child class that also includes thesis title.

I also added a method to calculate GPA from a list of grades. At the end, I created one student and tested everything to make sure it works.

### 2. `file_handling.py`
This file helps with saving and reading student records from a text file.

I wrote two main functions:
- `write_students()` → saves student info to a file.
- `read_students()` → reads data back and shows it on screen.

I also added error messages in case the file is missing or something goes wrong.

### 3. `student_utils/` (My Own Python Package!)
Here I made a custom Python package with three simple modules:
- `arithmetic.py` → calculates percentage and assigns grades.
- `attendance.py` → finds attendance percentage.
- `performance.py` → tells if a student is doing "Excellent", "Good", or "Needs Improvement" based on GPA.

There’s also a `main.py` file that uses all these functions to check if they’re working.

### 4. `iterators_generators.py`
In this file, I practiced:
- **Iterator** → to go through a list of students one by one.
- **Generator 1** → to randomly mark students as "Present" or "Absent".
- **Generator 2** → to give random marks (just for testing).

It was fun trying these things out and now I understand how iterators and generators work!

##  What I Learned
- How to write Python classes using OOP and inheritance.
- How to read and write from files safely.
- How to make my own Python package with multiple modules.
- What iterators and generators are, and how to use them in real situations.

## Notes
I kept every file simple and added some comments to explain what’s happening.

Also, I tested each file using this condition:
```python
if __name__ == "__main__":

So that I could run each one separately and check if it works fine.

Thanks for checking my project! 

