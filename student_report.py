from student import Student

class StudentReportGenerator:
    def generate(self, student: Student) -> str:
        return f"""
ID: {student.id}
Name is: {student.name}
Grades Count: {len(student.gradez)}
Average: {student.gradez.calc_average():.2f}
Final Grade = {student.letter}
Passed: {student.is_passed}
Honor: {student.honor}
        """
    
    def print(self, student: Student) -> None:
        print("Student Report")
        print("============")
        print(self.generate(student))
        print("============")