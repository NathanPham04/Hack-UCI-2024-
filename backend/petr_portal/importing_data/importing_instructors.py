# importing_instructors.py
# 
# Importing UCI instructors from Petr Portal API

import requests

from create_csv import write_data_to_csv



# Uses Pandas to write instructor data to csv
def _write_instructor_data_to_csv() -> None:
    columns = ["shortened_name", "name", "ucinetid", "department"]
    data = _get_instructor_data()

    write_data_to_csv(data, columns, "instructor_data.csv")

# Returns data about each instructor
def _get_instructor_data() -> list[list]:
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



if __name__ == "__main__":
    # _write_instructor_data_to_csv()
    pass