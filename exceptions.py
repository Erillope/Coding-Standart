
class GradezIndexError(Exception):
    """Exception raised for errors in the grade index."""
    @classmethod
    def from_index(cls, index: int) -> 'GradezIndexError':
        return cls(f"No existe la calificación en el índice proporcionado: {index}.")