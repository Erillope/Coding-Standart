
class GradezError(Exception):
    @classmethod
    def from_index(cls, index: int) -> 'GradezError':
        return cls(f"No existe la calificación en el índice proporcionado: {index}.")
    
    @classmethod
    def invalid_grade(cls, grade: int) -> 'GradezError':
        return cls(f"La calificación proporcionada no es válida: {grade}. Debe ser un número entero entre 0 y 100.")
    
    @classmethod
    def grade_not_found(cls, grade: int) -> 'GradezError':
        return cls(f"La calificación {grade} no se encuentra en la lista de calificaciones.")

class IDError(Exception):    
    @classmethod
    def empty_id(cls) -> 'IDError':
        return cls("El ID no puede estar vacío.")