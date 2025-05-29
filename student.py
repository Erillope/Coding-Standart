from grade import Grades
from id import ID

class Student:
    def __init__(self, id: str, name: str) -> None:
        self.id= ID(id)
        self.name =name
        self.gradez = Grades()
        self.is_passed = "NO"
        self.honor = "?"
        self.letter = "F"
        
    def check_honor(self) -> None:
        if self.gradez.calc_average()>90:
            self.honor = "yep"
        else:
            self.honor = "nope"