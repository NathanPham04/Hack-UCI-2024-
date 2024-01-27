# importing_grades.py
# 
# Importing UCI grades from Petr Portal API

import requests
import datetime
import pandas

from create_csv import write_data_to_csv

# Gets grade data from the last 5 years
def _get_all_grade_data() -> None:
    today = datetime.datetime.today()
    year = getattr(today, "year")
    month = getattr(today, "month")

    # EX: Jan 2024 -> 2023-24
    # EX: Dec 2023 -> 2023-24
    if month < 9:
        year-= 1

    # data = [course, instructor, grades]

    for i in range(6):
        # EX: school_year = "2023-24"
        school_year = f"{year - i}-{year - i + 1 - 2000}"
        print(f"Gathering data from the year {school_year}")

        _get_grade_data(school_year)



    


def _get_grade_data(year: str) -> None:

    # creating DataFrame from grades.csv
    df = pandas.read_csv("data/grade_data.csv")

    # get json data from Petr Portal
    url = "https://api.peterportal.org/rest/v0/grades/raw?"
    url+= "year=" + year
    response = requests.get(url)
    json = response.json()

    # pull all course grade data
    for course in json:
        course_name = "".join((course["department"] + course["number"]).split(" "))
        instructor = course["instructor"]

        # mask is a condition to find ceratin values
        mask = (df["course_id"] == course_name) & (df["instructor"] == instructor)

        # add to DataFrame if not already in
        if df[mask].empty:
            grade_data = {
                "course_id": course_name,
                "instructor": instructor,
                "gradeACount": course["gradeACount"],
                "gradeBCount": course["gradeBCount"],
                "gradeCCount": course["gradeCCount"],
                "gradeDCount": course["gradeDCount"],
                "gradeFCount": course["gradeFCount"],
                "gradePCount": course["gradePCount"],
                "gradeNPCount": course["gradeNPCount"]
            }
            df.loc[len(df)] = grade_data
        # update grades in DataFrame if already existing
        else:
            for letter_grade in ["A", "B", "C", "D", "F", "P", "NP"]:
                df.loc[mask, f"grade{letter_grade}Count"]+= int(course[f"grade{letter_grade}Count"])

        # save df to already existing .csv file
        df.to_csv("data/grade_data.csv", index=False)




if __name__ == "__main__":
    _get_all_grade_data()