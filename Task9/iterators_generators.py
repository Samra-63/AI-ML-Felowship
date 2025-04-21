# practicing some cool stuff like iterators and generators 
import random
class StudentList:
    def __init__(self, students):
        self.students = students
        self.index = 0 
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student
# Generator to randomly simulate present/absent
def attendance_generator(students):
    for student in students:
        status = random.choice(["Present", "Absent"])
        yield f"{student} is {status}"
# Generator to give random marks (just for fun/testing)
def random_marks_generator(count):
    for _ in range(count):
        yield random.randint(50, 100)
# testing all the above stuff
if __name__ == "__main__":
    names = ["Samra", "Ali", "Zara", "Ahmed"]

    print("Iterating Students:")
    for s in StudentList(names):
        print(s)

    print("\nAttendance Simulation:")
    for status in attendance_generator(names):
        print(status)

    print("\nRandom Marks:")
    for marks in random_marks_generator(5):
        print("Marks:", marks)
