from exceptions import GradezError
from typing import List

class Grades:
    def __init__(self) -> None:
        self.gradez: List[int] = []
    
    def add_grade(self, grade: int) -> None:
        self.__validate_grade(grade)
        self.gradez.append(grade)
    
    def delete_grade(self, index: int) -> None:
        self.__validate_index(index)
        del self.gradez[index]
    
    def delete_grade_by_value(self, grade: int) -> None:
        if grade not in self.gradez:
            raise GradezError.grade_not_found(grade)
        self.gradez.remove(grade)
    
    def calc_average(self) -> float:
        if not self.gradez:
            return 0.0
        total = sum(self.gradez)
        return total / len(self.gradez)
    
    def __validate_grade(self, grade: int) -> None:
        if not grade in range(0, 101):
            raise GradezError.invalid_grade(grade)
    
    def get(self) -> List[int]:
        return self.gradez
    
    def __len__(self) -> int:
        return len(self.gradez)
    
    def __validate_index(self, index: int) -> None:
        if index < 0 or index >= len(self.gradez):
            raise GradezError.from_index(index)