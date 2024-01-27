# professors.py
# 
# Creates a list of all UCI instructor names from Petr Portal API

# pip install requests
import requests
import pandas


# Returns data about each instructor
def get_instructor_data():
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
def write_instructor_data_to_csv():
    data = get_instructor_data()
    columns = ["shortened_name", "name", "ucinetid", "department"]

    # create pandas DataFrame
    df = pandas.DataFrame(data, columns=columns)


    df.to_csv("data/instructor_data.csv", index=False)



if __name__ == "__main__":
    write_instructor_data_to_csv()