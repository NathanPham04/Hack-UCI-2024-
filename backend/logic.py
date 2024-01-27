class Gate:
    def __init__(self, obj1, obj2) -> None:
        self.obj1 = obj1
        self.obj2 = obj2

    def verfiy(self) -> bool:
        pass


class And(Gate):
    def __init__(self, obj1, obj2) -> None:
        super().__init__(obj1, obj2)
    
    def verfiy(self) -> bool:
        return super().obj1.verify() and super().obj2.verify()


class Or(Gate):
    def __init__(self, obj1, obj2) -> None:
        super().__init__(obj1, obj2)

    def verfiy(self) -> bool:
        return super().obj1.verify() or super().obj2.verify()