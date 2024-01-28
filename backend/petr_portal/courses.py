# courses.py
# 
# Provides functions to retreive course data about classes

import pandas


# Provides a list of all ge classes, given any categories
def get_all_needed_ge_classes(*args: str):
    all_classes = set()
    for arg in args:
        all_classes.update(get_ge_classes(arg))
    
    return all_classes


# Provides a list of all ge classes under a given category
#   ge_category: str
def get_ge_classes(ge_category: str) -> set[str]:
    searching_for = ""
    match ge_category:
        case "Ia":
            searching_for = "GE Ia: Lower Division Writing"
        case "Ib":
            searching_for = "GE Ib: Upper Division Writing"
        case "II":
            searching_for = "GE II: Science and Technology"
        case "III":
            searching_for = "GE III: Social & Behavioral Sciences"
        case "IV":
            searching_for = "GE IV: Arts and Humanities"
        case "Va":
            searching_for = "GE Va: Quantitative Literacy"
        case "Vb":
            searching_for = "GE Vb: Formal Reasoning"
        case "VI":
            searching_for = "GE VI: Language Other Than English"
        case "VII":
            searching_for = "GE VII: Multicultural Studies"
        case "VIII":
            searching_for = "GE VIII: International/Global Issues"
        case _:
            return

    # creating DataFrame from course_data.csv
    df = pandas.read_csv("data/course_data.csv")
    mask = (df["ge_list"].str.contains(searching_for, na=False))
    result = df.loc[mask, "id"]

    return(set(result))
    


if __name__ == "__main__":
    print(get_all_needed_ge_classes("Va", "Vb"))