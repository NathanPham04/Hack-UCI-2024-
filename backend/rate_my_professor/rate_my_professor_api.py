import ratemyprofessor
# aapi = RMPClass.RateMyProfAPI(schoolId=45, teacher="xxx")
# aapi.retrieveRMPInfo()


from itertools import islice
import csv

# Specify the path to your CSV file
csv_file_path = '../../data/instructor_data.csv'

# List to store full names
full_names = []

# Open the CSV file and read the data
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the header
    next(csv_reader)

    # Iterate through the rows and extract full names
    for row in csv_reader:
        full_name = row[1]  # Assuming the full name is in the first column
        full_names.append(full_name)
schools = ratemyprofessor.get_school_by_name("UCI")
# Print the extracted full names
# for name in full_names:
with open("rate_my_professor_data.csv", 'a', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

        # Write header
    # csv_writer.writerow(['Name', 'Rating', 'Difficulty'])
    for name in full_names[1300:1399]:#start at 1400

            professor = ratemyprofessor.get_professor_by_school_and_name(schools, name) 
            if hasattr(professor, 'name') and hasattr(professor, 'rating') and hasattr(professor, 'difficulty'):
                print(professor.name, professor.rating, professor.difficulty)
                csv_writer.writerow([professor.name, professor.rating, professor.difficulty])
            # else:
                # print("The professor object does not have 'name' and 'rating' and 'difficulty' attributes.")
        # print(professor.rating)