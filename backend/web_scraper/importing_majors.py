# importing_majors.py
# 
# Importing UCI major requirements from web scraping

import requests
import datetime
import pandas

# Gets imports major data into a .csv
def write_major_data_to_csv() -> None:

    # dict: {major_name: [classes...]}
    # major_requirements = get_major_requirements()
    major_requirements = {
        "computerscience": ["I&C SCI 45C", "I&C SCI 46"],
        "biomedicalengineering": ["CHEM1A", "CHEM1AL", "CHEM1B", "CHEM1BL"]
    }
    
    # formats the major requirements for pandas import
    formatted_requirements = {
        "major": [major for major in major_requirements],
        # vvv   gets ride of spaces in courses, "I&C SCI 46" -> "I&CSCI46"   vvv
        "required_classes": [["".join((course).split(" ")) for course in major_requirements[major]] for major in major_requirements]
    }

    print(formatted_requirements)

    # creating DataFrame from grade_data.csv
    df = pandas.DataFrame(formatted_requirements)

    # create new .csv files
    df.to_csv(("data/major_data.csv"), index=False)




if __name__ == "__main__":
    write_major_data_to_csv()