# professors.py
# 
# Creates a list of all UCI instructor names from Petr Portal API

# pip install requests
import requests
import pandas

# Creates a .csv file with the given data
def _write_data_to_csv(data, columns, file_name):
    # create pandas DataFrame
    df = pandas.DataFrame(data, columns=columns)

    # create new csv files
    df.to_csv(("data/" + file_name), index=False)


# Returns data about each instructor
def _get_instructor_data():
    # get json data from Petr Portal
    url = "https://api.peterportal.org/rest/v0/instructors/all"
    response = requests.get(url)
    json = response.json()

    # place all names into a list
    data = list()
    for instructor in json:
        row = []
        row.append(instructor["shortened_name"])
        row.append(instructor["name"])
        row.append(instructor["ucinetid"])
        row.append(instructor["department"])

        data.append(row)

    data.sort()

    return data

# Uses Pandas to write instructor data to csv
def _write_instructor_data_to_csv():
    columns = ["shortened_name", "name", "ucinetid", "department"]
    data = _get_instructor_data()

    _write_data_to_csv(data, columns, "instructor_data.csv")



# Returns data about each course
def _write_course_data_to_csv():
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

    _write_data_to_csv(data, columns, "course_data.csv")

# TODO
# def 



if __name__ == "__main__":
    pass