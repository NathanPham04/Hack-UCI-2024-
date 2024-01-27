import logic


class Course:
    def __init__(self, course_code, pre_req_tree : str, ge : list(str), taken : bool) -> None:
        self.course_code = course_code
        self.pre_req_tree = pre_req_tree
        self.ge = ge
        self.taken = taken

    
    def check_takeability(self, courses_taken : set{Course}):
        # tokenize pre req tree AND(OR(stats 67, stsats 7), math 2b)    

        pass

    def verify(self):
        return self.taken


    
def tokenize(loigcal_expression : str):
    pass


class Major:
    def __init__(self, name, requirements) -> None:
        self._name = name
        self._requirements = requirements

    @property
    def name(self):
        return self._name
    

    @property
    def requirements(self):
        return self._requirements
    

    