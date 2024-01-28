# importing_courses.py
# 
# Importing UCI courses from Petr Portal API

import requests

from create_csv import write_data_to_csv


# Returns data about each course
def _write_course_data_to_csv() -> None:
    # get json data from Petr Portal
    url = "https://api.peterportal.org/rest/v0/courses/all"
    response = requests.get(url)
    json = response.json()

    data = list()
    for course in json:
        row = []
        for key in course:
            row.append(course[key])

        data.append(row)

    columns = [column for column in json[0]]

    write_data_to_csv(data, columns, "course_data.csv")



if __name__ == "__main__":
    # _write_course_data_to_csv()
    pass