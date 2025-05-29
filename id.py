from exceptions import IDError

class ID:
    def __init__(self, id: str) -> None:
        if id.strip() == "":
            raise IDError.empty_id()
        self.id = id
    
    def get(self) -> str:
        return self.id