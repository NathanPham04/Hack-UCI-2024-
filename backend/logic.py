class Gate:
    def __init__(self, courses : list) -> None:
        self.courses = courses

    def __repr__(self) -> str:
        pass

    def __bool__(self) -> bool:
        pass


class And(Gate):
    def __init__(self, courses) -> None:
        super().__init__(courses)

    def __repr__(self) -> str:
        return f"And({self.courses})"
    
    def __bool__(self) -> bool:
        return all(self.courses)


class Or(Gate):
    def __init__(self, courses) -> None:
        super().__init__(courses)

    def __repr__(self) -> str:
        return f"Or({self.courses})"

    def __bool__(self) -> bool:
        return any(self.courses)