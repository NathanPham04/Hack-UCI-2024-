# user.py
#
# Everything about the user

import pandas

import web_scraper.web_scraper
import petr_portal.courses
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
        self._major = ()
        self._needed_ges = {}  # Ex: Ia, III, Vb, etc.

        # some default values
        self._min_units = 12
        self._max_units = 18
        
    # passes in the major in the format that it appears in the url
    # EX: computerscience_bs
    def set_major(self, major: str) -> None:
        pass
        # # check that the major exists
        # df = pandas.read_csv("data/grade_data.csv")

        # url = 
        # self.major = major

    # returns all potential classes to work towards graduating
    def get_potential_classes():
        # get major classes
        # add ge classes
        # subtract invalid to take
        # return
        pass
