# courses.py
# 
# Provides functions to retreive course data about classes

import pandas





# Provides a list of all ge classes under a given category
#   ge_category: str
#       "Ia"    |  Lower-Division Writing
#       "Ib"    |  Upper-Division Writing
#       "II"    |  Science and Technology
#       "III"   |  Social and Behavioral Sciences
#       "IV"    |  Arts and Humanities
#       "Va"    |  Quantitative, Symbolic & Computat'l Reasoning
#       "Vb"    |  Formal Reasoning
#       "VI"    |  Language
#       "VII"   |  Multicultural Studies
#       "VIII"  |  Int'l/Global Issues
def get_ge_classes(ge_category: str):
    searching_for = f"GE {ge_category}: "

    # creating DataFrame from course_data.csv
    df = pandas.read_csv("data/course_data.csv")
    mask = (df["course_id"] == course) & (df["instructor"] == instructor)
    result = df.loc[mask]
    
    match ge_category:
        case "Ia":

        case _:
            return