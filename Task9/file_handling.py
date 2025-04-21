# This file deals with reading and writing student data to text files
# (basically saving stuff and getting it back later)
def read_students(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print("Here are the students from the file:\n")
            for line in lines:
                print(line.strip())  
            print(f"\nTotal Students in File: {len(lines)}")   
    except FileNotFoundError:
        print("Uh oh 😬... The file was not found.") 
    except Exception as e:
        print("Something went wrong while reading the file:", str(e))
def write_students(filename, students_list):
    try:
        with open(filename, 'w') as file:
            for student in students_list:
                file.write(student + "\n")  
        print(f"Data has been written to {filename} successfully!")
    except Exception as e:
        print("Error while writing to file:", str(e))
# just testing the above functions here 👇
if __name__ == "__main__":
    students = [
        "Samra,22,CS001,Python;ML",
        "Ali,23,CS002,Web;AI"
    ]
    write_students("student_output.txt", students)
    read_students("student_output.txt")
