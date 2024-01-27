# professors.py
# 
# Creates a list of all UCI instructor names from Petr Portal API

# pip install requests
import requests


def write_professors_to_file():
    
    # get json data from Petr Portal
    url = "https://api.peterportal.org/rest/v0/instructors/all"
    response = requests.get(url)
    json = response.json()

    # place all names into a list
    all_names = list()
    for instructor in json:
        name = instructor["name"].split(" ")

        first_initial = name[0][0]
        last_name = name[-1]

        all_names.append((last_name + ", " + first_initial + "." + "\n"))


    all_names.sort()

    # write sorted names to instructors.txt
    with open("backend/petr_portal/instructors.txt", "x") as instructor_file:
        for name in all_names:
            instructor_file.write(name)


        


if __name__ == "__main__":
    pass