# This is my Student Management System using OOP concepts
# I'm just creating classes and testing how things work in real life :)
class Student:
    def __init__(self, name, age, student_id, courses):
        self._name = name
        self._age = age
        self._student_id = student_id
        self._courses = courses  
    #  name
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    #  age
    def get_age(self):
        return self._age
    def set_age(self, age):
        self._age = age
    #  ID
    def get_student_id(self):
        return self._student_id
    def set_student_id(self, student_id):
        self._student_id = student_id
    #  courses list
    def get_courses(self):
        return self._courses

    def set_courses(self, courses):
        self._courses = courses

    # method to calculate GPA from list of grades
    def calculate_gpa(self, grades):
        if len(grades) == 0:
            return 0.0 
        return sum(grades) / len(grades) 


# subclass for graduate students
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, courses, thesis_title):
        super().__init__(name, age, student_id, courses)
        self.thesis_title = thesis_title

    def __str__(self):
        # this will print all the student info in a nice way
        return f"Name: {self._name}, Age: {self._age}, ID: {self._student_id}, Courses: {self._courses}, Thesis: '{self.thesis_title}'"


# just testing it out here 👇
if __name__ == "__main__":
    # sample student
    my_student = GraduateStudent("Samra", 22, "CS001", ["Python", "AI"], "Sign Language Recognition")

    print(my_student)  # calling __str__ method automatically
    print("GPA is:", my_student.calculate_gpa([3.5, 3.7, 4.0])) 
