# user.py
#
# Everything about the user

import pandas

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
    


    # returns all potential classes to work towards graduating
    def get_potential_classes(self):
        all_classes = set()

        # get major classes
        if self._major != None:
            all_classes = self._major.requirements # list of requirements 

        # add ge classes
        all_classes.update(courses.get_all_needed_ge_classes(*self._needed_ges))

        self._remove_invalid(all_classes)

        return all_classes
        




if __name__ == "__main__":
    user = User()
    user.set_major("Business Information Management")
    # user._needed_ges = ["II", "III"]

    print(user.get_potential_classes())