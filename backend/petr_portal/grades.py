# grades.py
# 
# Provides functions to retreive grade data about classes

import pandas



# Returns GPA of each grade
def get_avereage_gpa(course: str, instructor: str) -> float:
    # creating DataFrame from grades.csv
    df = pandas.read_csv("data/grade_data.csv")
    mask = (df["course_id"] == course) & (df["instructor"] == instructor)
    result = df.loc[mask]
    
    letter_grades = ["F", "D", "C", "B", "A"]

    total_grade_points = 0
    total_students = 0
    for i in range(5):
        total_grade_points+= int(result[f"grade{letter_grades[i]}Count"]) * i
        total_students+= int(result[f"grade{letter_grades[i]}Count"])
    
    
    if total_students <= 0:
        return None
    
    return total_grade_points / total_students



if __name__ == "__main__":
    print(get_avereage_gpa("I&CSCI6B", "GASSKO, I."))