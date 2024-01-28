# user.py
#
# Everything about the user

import pandas

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
        self.taken_classes = set()
        # self.major = Major("")
        # self.needed_ges = {}  # Ex: Ia, III, Vb, etc.
        # self.unit_min = 0
        # self.unit_max = 100
        
    def change_major(self, major: str) -> None:
        self.major = major