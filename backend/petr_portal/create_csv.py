# create_csv.py
#
# Creates a .csv file with the given data

import pandas


def write_data_to_csv(data, columns, file_name):
    # create pandas DataFrame
    df = pandas.DataFrame(data, columns=columns)

    # create new csv files
    df.to_csv(("data/" + file_name), index=False)

