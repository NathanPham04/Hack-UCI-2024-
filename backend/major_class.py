import logic
import re

class Professor:
    def __init__(self, name, rating, difficulty) -> None:
        self.name = name
        self.rating = rating
        self.difficulty = difficulty
        self.times = dict()

    def set_times(self, **kwargs):
        self.times = kwargs

    def get_optimality(self) -> int:
        pass 


    # Course.professor[0].times[Course.course_code]




class Course:
    def __init__(self, course_code, pre_req_tree : str, ge : list[str], taken : bool, profs) -> None:
        self.course_code = course_code
        self.pre_req_tree = pre_req_tree
        self.ge = ge
        self.taken = taken
        self.professor = profs

    def __repr__(self) -> str:
        return f"Course({self.course_code}, {self.pre_req_tree}, {self.ge}, {self.taken})"

    def __bool__(self) -> bool:
        return self.taken
    
    @staticmethod
    def get_optimal():
        pass


    
def tokenize(logical_expression : str, operator : str = "AND") -> logic.Gate:
    pass
    # if operator == "AND":
    #     p = r'({""AND"":\[{["A-Za-z0-9 &,:\[\]]+.+?(?=}")})|({""AND"":\[["A-Za-z0-9 &,{}:\[\]]+\]})'
    # else:
    #     p = r'({""OR"":\[{["A-Za-z0-9 &,:\[\]]+.+?(?=}")})|({""OR"":\[["A-Za-z0-9 &,{}:\[\]]+\]})'

    # processed_exp = re.search(string = logical_expression, pattern = p)
    # if processed_exp is not None:
    #     processed_exp = processed_exp.group()[9:-1]
    #     print("processed (AND):", processed_exp)

    #     raw_courses = re.search(string = processed_exp, pattern = '("".+?(?=\{))|(\[["A-Z& 0-9,]+\])')
    #     if raw_courses is not None:
    #         tmp = re.findall(string = raw_courses.group(), pattern = '([A-Z&0-9]{3,} [A-Z]* [0-9]+[A-Z]*)|([A-Z]{3,} [0-9]+[A-Z]*)')
    #     else:
    #         tmp = re.findall(string = processed_exp, pattern = '([A-Z&0-9]{3,} [A-Z]* [0-9]+[A-Z]*)|([A-Z]{3,} [0-9]+[A-Z]*)')


    #     courses = []

    #     for c in tmp:
    #         courses += filter(lambda x : x != "", c)

    #     processed_courses = []

    #     if "AND" in processed_exp or "OR" in processed_exp:
    #         processed_courses.append(tokenize(processed_exp))

    #     for course in courses:
    #         temp_pre_req = "REPLACE THIS"

    #         processed_courses.append(Course(course, temp_pre_req, [""], False))
        
    #     return logic.And(processed_courses)
    




def valid_parens(string):
    opening = "[", "(", "{"
    closing = "]", ")", "}"
    matches = [[opening[i], closing[i]] for i in range(3)]

    stack = []
    for c in string:
        if c in opening:
            stack.append(c)
        elif c in closing:
            if (len(stack) == 0) or (not [stack.pop(), c] in matches):
                return False
            
    return len(stack) == 0




class Major:
    def __init__(self, name, requirements : list[Course]) -> None:
        self._name = name
        self._requirements = requirements

    @property
    def name(self):
        return self._name
    

    @property
    def requirements(self):
        return self._requirements
    

    
if __name__ == "__main__":
    # tmp = tokenize('"{""AND"":[""MATH 2D"",{""OR"":[""MATH 3A"",""MATH 6G""]}]}"')
    tmp = tokenize('"{""AND"":[{""OR"":[""CSE 46"",""I&C SCI 46""]},{""OR"":[""MATH 2B"",""AP CALCULUS BC""]},{""OR"":[""STATS 67"",{""AND"":[""STATS 120A"",{""OR"":[""STATS 7"",""AP STATISTICS""]}]}]}]}"')
    print(tmp)

    
    # tokenize("{""OR"":[""MATH 2B"",""MATH 5B"",""MATH 7B"",""AP Calculus BC""]}")