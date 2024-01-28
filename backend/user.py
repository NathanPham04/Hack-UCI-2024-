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
        self._major = None
        self._needed_ges = {}  # Ex: Ia, III, Vb, etc.
        self._needed_classes = {}

        # some default values
        self._min_units = 12
        self._max_units = 18
        
    # passes in the major in the format that it appears in the url
    # EX: computerscience_bs
    def set_major(self, major: str) -> None:
        all_urls = x = web_scraper.get_urls("backend/web_scraper/result.html")
        major_url
        for url in all_urls:
            if f"/{major}/" in url:
                major_url = url
        self.major = major