import logic
import re

class Course:
    def __init__(self, course_code, pre_req_tree : str, ge : list[str], taken : bool) -> None:
        self.course_code = course_code
        self.pre_req_tree = pre_req_tree
        self.ge = ge
        self.taken = taken

    def __repr__(self) -> str:
        return f"Course({self.course_code}, {self.pre_req_tree}, {self.ge}, {self.taken})"

    def __bool__(self) -> bool:
        return self.taken
    
    # def check_takeability(self, courses_taken : set{Course}):
    #     # tokenize pre req tree AND(OR(stats 67, stsats 7), math 2b)    

    #     pass

    def verify(self):
        return self.taken

"{""AND"":[""I&C SCI 33"",""I&C SCI 6B""]}"
"{""OR"":[""MATH 2B"",""MATH 5B"",""MATH 7B"",""AP Calculus BC""]}"
    
def tokenize(logical_expression : str) -> logic.Gate:
    first_operator = get_first_operator(logical_expression)

    if first_operator == "AND":
        p = r'({""AND"":\[{["A-Za-z0-9 &,:\[\]]+.+?(?=}")})|({""AND"":\[["A-Za-z0-9 &,{}:\[\]]+\]})'
    else:
        p = r'({""OR"":\[{["A-Za-z0-9 &,:\[\]]+.+?(?=}")})|({""OR"":\[["A-Za-z0-9 &,{}:\[\]]+\]})'

    processed_exp = re.search(string = logical_expression, pattern = p)
    if processed_exp is not None:
        processed_exp = processed_exp.group()[9:-1]
        print(f"processed ({first_operator}):", processed_exp)

        raw_courses = re.search(string = processed_exp, pattern = '("".+?(?=\{))|(\[["A-Z& 0-9,]+\])')
        if raw_courses is not None:
            print("AAAAAAAAAAAAAAAAAAAAAAAA", raw_courses.group())
            tmp = re.findall(string = raw_courses.group(), pattern = '([A-Z&0-9]{3,} [A-Z]* [0-9]+[A-Z]*)|([A-Z]{3,} [0-9]+[A-Z]*)')
        else:
            tmp = re.findall(string = processed_exp, pattern = '([A-Z&0-9]{3,} [A-Z]* [0-9]+[A-Z]*)|([A-Z]{3,} [0-9]+[A-Z]*)')


        courses = []

        print("BBBBBBBBBBBBBBBBBBBB", tmp)

        for c in tmp:
            courses += filter(lambda x : x != "", c)

        processed_courses = []

        if "AND" in raw_courses.group():
            processed_courses.append(tokenize(processed_exp))
        elif "OR" in raw_courses.group():
            processed_courses.append(tokenize(processed_exp))

        print("courses", courses, "operator:", first_operator)
        for course in courses:
            temp_pre_req = "REPLACE THIS"

            processed_courses.append(Course(course, temp_pre_req, [""], False))
        
        if first_operator == "AND":
            return logic.And(processed_courses)
        elif first_operator == "OR":
            return logic.Or(processed_courses)
        else:
            return None  # this is bad and shouldn't happen
    
def get_first_operator(string : str) -> str:
    lowercased_string = string.lower()

    # Find the indices of "and" and "or"
    and_index = lowercased_string.find("and")
    or_index = lowercased_string.find("or")

    # Check which one appears first or if neither appears
    if and_index != -1 and (or_index == -1 or and_index < or_index):
        return "AND"
    elif or_index != -1 and (and_index == -1 or or_index < and_index):
        return "OR"
    else:
        return "Neither"

    # processed_exp = re.search(string = logical_expression, pattern = r'({""OR"":\[{["A-Za-z0-9 &,:\[\]]+.+?(?=}")})|({""OR"":\[["A-Za-z0-9 &,{}:\[\]]+\]})')
    # if processed_exp is not None:
    #     processed_exp = processed_exp.group()[8:-1]
    #     print("processed (AND):", processed_exp)

    #     # print("processed courses:", processed_exp)
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
        
    #     return logic.Or(processed_courses)



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
    def __init__(self, name, requirements) -> None:
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
    tmp = tokenize('"WRITING 60, OR"":[""MATH 2B"",""AP CALCULUS BC""]},{""OR"":[""STATS 67"",{""AND"":[""STATS 120A"",{""OR"":[""STATS 7"",""AP STATISTICS""]}]}]}]}"')
    print("expression:", tmp)

    

    
    # tokenize("{""OR"":[""MATH 2B"",""MATH 5B"",""MATH 7B"",""AP Calculus BC""]}")