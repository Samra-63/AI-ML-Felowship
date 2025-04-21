# testing my custom package called student_utils (which I made btw )
from student_utils import arithmetic, attendance, performance
if __name__ == "__main__":
    # checking percentage and grade
    percent = arithmetic.calculate_percentage(460, 500)
    grade = arithmetic.classify_grade(percent)
    print("Percentage:", round(percent, 2))
    print("Grade:", grade)
    att_percent = attendance.attendance_percentage(22, 25)
    print("Attendance %:", round(att_percent, 2))
    # performance based on GPA
    performance_msg = performance.evaluate_performance([3.5, 3.8, 3.4])
    print("Performance:", performance_msg)
