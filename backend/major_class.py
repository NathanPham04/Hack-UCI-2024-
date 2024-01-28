import logic
import re
import json
import pandas

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
    

    
def format_json(string):
    string = string.replace('""', '"')
    # string = string.replace("[", "{")
    # string = string.replace("]", "}")
    return string
    


def tokenize(logical_expression : str) -> logic.Gate:
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
                    contents.append(value)
            
            if key == "AND":
                return logic.And(contents)
            elif key == "OR":
                return logic.Or(contents)
            

    return recursive_tokenize(temp)




class Major:
    def __init__(self, name) -> None:
        self._name = name

        # read requirements from major_data.csv

        df = pandas.read_csv("./data/major_data.csv")
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
    