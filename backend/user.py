# user.py
#
# Everything about the user

import web_scraper.web_scraper
from petr_portal.courses import get_all_needed_ge_classes
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
        self._needed_ges = []  # Ex: Ia, III, Vb, etc.

        # some default values
        self._min_units = 12
        self._max_units = 18
        
    # passes in the major in the format that it appears in the url
    # EX: computerscience_bs
    def set_major(self, major: str) -> None:
        self._major = Major(major)

    # returns all potential classes to work towards graduating
    def get_potential_classes(self):
        all_classes = set()

        # get major classes
        if self._major != None:
            all_classes = self._major.requirements # list of requirements 

        # add ge classes
        all_classes.update(get_all_needed_ge_classes(*self._needed_ges))

        # subtract invalid to take

        return all_classes




if __name__ == "__main__":
    user = User()
    user.set_major("Business Information Management")
    user._needed_ges = ["II"]

    print(user.get_potential_classes())