from typing import List
from exceptions import GradezIndexError

class Student:
    def __init__(self, id: str, name: str) -> None:
        self.id=id
        self.name =name
        self.gradez: List[int] = []
        self.is_passed = "NO"
        self.honor = "?"
        self.letter = "F"
        
    def add_grades(self, g: int) -> None:
        self.gradez.append(g)
        
    def calc_average(self) -> float:
        t=0
        for x in self.gradez:
            t+=x
        avg = t / len(self.gradez) if self.gradez else 0
        return avg
            
    def check_honor(self) -> None:
        if self.calc_average()>90:
            self.honor = "yep"
            
    def delete_grade(self, index: int) -> None:
        if index < 0 or index >= len(self.gradez):
            raise GradezIndexError.from_index(index)
        del self.gradez[index]
        
    def report(self) -> None: # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.gradez)))
        print("Final Grade = " + self.letter)
        
def start_run() -> None:
    a = Student("x","")
    a.add_grades(100)
    a.add_grades(50) # broken
    a.calc_average()
    a.check_honor()
    a.delete_grade(5) # IndexError
    a.report()
    
start_run()