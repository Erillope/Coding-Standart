from student import Student
from student_report import StudentReportGenerator

def start_run() -> None:
    student = Student("xs","")
    student.gradez.add_grade(100)
    student.gradez.add_grade(50)
    student.gradez.calc_average()
    student.check_honor()
    #student.gradez.delete_grade(5)
    #student.gradez.delete_grade_by_value(50)
    report_generator = StudentReportGenerator()
    report_generator.print(student)
    
start_run()