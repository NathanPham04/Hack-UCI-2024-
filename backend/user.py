# user.py
#
# Everything about the user

import pandas
import csv

import web_scraper.web_scraper
from petr_portal import courses
import major_class
import petr_portal.grades
from major_class import Course, Major


# Contains...
#   Classes taken
#   Major
#   GE's needed
#   Desired units
#   Desired class time
class User:
    def __init__(self) -> None:
        self._taken_classes = set()
        self._major = None
        self._needed_ges = {}  # Ex: Ia, III, Vb, etc.

        # some default values
        self._min_units = 12
        self._max_units = 18
        
    # passes in the major in the format that it appears in the url
    # EX: computerscience_bs
    def set_major(self, major: str) -> None:
        self._major = Major(major)

    # takes a set of ge categories that are still needed
    def set_needed_ges(self, *args) -> None:
        ge_categories = {"Ia", "Ib", "II", "III", "IV", "Va", "Vb", "VI", "VII", "VIII"}

        needed_ges = set()

        for arg in args:
            if arg in ge_categories:
                self._needed_ges.add(arg)
    
    def get_classes_taken(self):
        classes_taken = set()
        classes_taken.add("MGMT101")
        classes_taken.add("STATS110")
        return classes_taken

    def remove_invalid(self,all_classes):#,classes_taken):
        classes_taken = self.get_classes_taken()
        all_classes_copy = all_classes.copy()
        # for element in all_classes:
        #     print(element)
        for element_taken in classes_taken:
            for element_all in all_classes_copy:
                if element_taken == element_all:
                    all_classes.discard(element_taken) #in all_classes
                

    # returns all potential classes to work towards graduating
    def get_potential_classes(self):
        all_classes = set()

        # get major classes
        if self._major != None:
            all_classes = self._major.requirements # list of requirements 

        # add ge classes
        all_classes.update(courses.get_all_needed_ge_classes(*self._needed_ges))

        self.remove_invalid(all_classes)

        return all_classes
        
def find_prof_from_id(all_classes):
    with open("../data/grade_data.csv", 'r') as file:
        reader = csv.DictReader(file)
        all_rows = list(reader)
        instructors = dict()
        for element in all_classes:
            instructors[element] = "None"
        for element in all_classes:
            for row in all_rows:
                if row['course_id'] == element:
                    instructors[element] = row['instructor']
                # else:
                #     instructors[element] = "None"
        for key, value in instructors.items():
            print(f"Key: {key}, Value: {value}")
        return instructors
     # Return None if the course_id is not found


# if instructor is not None:
#     print(f"Instructor for course {course_id_to_find}: {instructor}")
# else:
#     print(f"Course ID {course_id_to_find} not found in the CSV.")
def get_prof_data(find_prof):
    #iterate through find prof
    #if it is None then print with none in user data csv
    # if its not none then try finding
    # if found then frind all the stats
    # if not then n/a
    with open("../data/user_data.csv", 'w') as file:
        file_writer = csv.writer(file)
        file_writer.writerow(['course_id', 'instructor', 'instructor_rating', 'instructor_gpa', 'instructor_difficulty'])
        # course_id,instructor,instructor_rating,instructor_gpa,instructor_difficuty
        for key, value in find_prof.items():
            if value == "None":
                file_writer.writerow([key, value, "None", "None", "None"])
            else:
                continue



if __name__ == "__main__":
    user = User()
    user.set_major("Business Information Management")
    user._needed_ges = ["II", "III"]

    # print(user.get_potential_classes())
    all_classes = user.get_potential_classes()
    print(all_classes)
    find_prof = find_prof_from_id(all_classes)
    prof_data = get_prof_data(find_prof)

