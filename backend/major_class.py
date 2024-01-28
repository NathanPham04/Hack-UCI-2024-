import logic
import re
import json
import pandas


class Professor:
    def __init__(self, name, rating, difficulty) -> None:
        self.name = name
        self.rating = rating
        self.difficulty = difficulty
        self.times = dict()     # key = class, value = times

    def set_times(self, **kwargs):
        self.times = kwargs

    def get_optimality(self) -> int:
        return self.rating 


class Course:
    def __init__(self, course_code, pre_req_tree : str, ge : list[str], taken : bool, professors : list[Professor], gpa : float) -> None:
        self.course_code = course_code
        self.pre_req_tree = pre_req_tree
        self.ge = ge
        self.taken = taken
        self.gpa = gpa
        self.professors = professors

        # sort professors based on a heuristic
        self.professors = list(sorted(self.professors, key = lambda x : 3 * x.rating - 2 * x.difficulty, reverse=True))

    def __repr__(self) -> str:
        return f"Course({self.course_code}, {self.pre_req_tree}, {self.ge}, {self.taken})"

    def __bool__(self) -> bool:
        return self.taken
    
    def get_rating(self):
        return self.professors[0].rating + 2 * self.gpa
    
    
    @classmethod
    def duplicate_course(cls, course : "Course"):
        profs = course.professors

        duplicates = []
        for p in profs:
            duplicates.append(cls(course.course_code, course.pre_req_tree, course.ge, course.taken, [p], course.gpa))
        
        return duplicates


    

    
def format_json(string):
    string = string.replace('""', '"')
    return string
    


def tokenize(logical_expression : str, courses_dict : dict) -> logic.Gate:
    print(format_json(logical_expression))
    temp = json.loads(format_json(logical_expression))

    def recursive_tokenize(logic_dict):
        contents = []
        for key, values in logic_dict.items():
            for value in values:
                if type(value) == dict:
                    contents.append(recursive_tokenize(value))
                else:
                    # pass in reference to courses taken dict
                    contents.append(courses_dict[value])
            
            if key == "AND":
                return logic.And(contents)
            elif key == "OR":
                return logic.Or(contents)
            

    return recursive_tokenize(temp)




class Major:
    def __init__(self, name) -> None:
        self._name = name

        # read requirements from major_data.csv

        df = pandas.read_csv("../data/major_data.csv")
        mask = (df["major_name"] == name)

        if df[mask].empty:
            self = None
            raise Exception("INVALID MAJOR")
            
        self._requirements = set(eval(list(df.loc[mask, "required_classes"])[0]))


    @property
    def name(self):
        return self._name
    

    @property
    def requirements(self):
        return self._requirements
    

if __name__ == "__main__":
    tmp = tokenize('{""AND"":[""MATH 2D"",{""OR"":[""MATH 3A"",""MATH 6G""]}]}')
    print(tmp)
    