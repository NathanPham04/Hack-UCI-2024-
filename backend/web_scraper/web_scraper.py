from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import pandas


BASE_URL = "https://catalogue.uci.edu"


def get_urls(file_path):
    urls = []
    with open(file_path, "r") as contents:
        for line in contents:
            # print(line)
            line = line.strip()
            if line.startswith("<li>"):
                tmp = re.search(pattern = '"(.*?)"', string = line)
                if tmp is not None:
                    tmp = tmp.group().strip('"')
                    if tmp.endswith("ba/") or tmp.endswith("bs/"):
                        urls.append(tmp)
                        print(tmp)

    # remove duplicates
    major_names = set()
    to_remove = []

    for i, url in enumerate(urls):
        name = get_major_name(url)
        if name in major_names:
            to_remove.append(i)
        
        else:
            major_names.add(name)

    to_remove.sort()

    for r in reversed(to_remove):
        urls.pop(r)

    
    return sorted(urls, key = lambda x : get_major_name(x))


def get_major_name(string):
    ret = []
    for i in range(len(string) - 2, -1, -1):
        if (string[i] == "/"):
            break

        ret.append(string[i])
    
    return "".join(list(reversed(ret)))


def get_requirements_from_url(url):
    """make sure it works with CS requirements"""

    driver = webdriver.Chrome()

    driver.get(BASE_URL + url)

    # page = driver.page_source.encode('utf-8')

    # tmp_file = open('result.html', 'wb')

    # tmp_file.write(page)

    # tmp_file.close()

    driver.find_element(By.ID,'requirementstexttab').click()

    tbody = driver.find_element(By.CLASS_NAME, 'sc_courselist')

    raw_data = []

    for tr in tbody.find_elements(By.XPATH, "//tr"):
        raw_data += [item.text for item in tr.find_elements(By.XPATH, "//td")]
        break

    refined_data = []

    for d in raw_data:
        if d != "":
            # print(d)
            tmp = re.search(string = d, pattern = '([A-Z]{3,} [0-9]+[A-Z]*\–[0-9]+[A-Z]*)|([A-Z]{3,} [0-9]+[A-Z]*- [0-9]+[A-Z]*)|([A-Z &]{3,} [0-9]+[A-Z]*)|(or [A-Z]{3,} [0-9]+[A-Z]*)')
            if tmp is not None:
                # print(tmp.group(), d)
                if tmp.group() == d:
                    tmp2 = re.search(string = d, pattern = '([A-Z]{3,} [0-9]+[A-Z]*- [0-9]+[A-Z]*)')
                    if tmp2 is not None and tmp2.group() == d:
                        department = re.search(string = d, pattern = '([A-Z]{3,})').group()
                        first_course = re.search(string = d, pattern = '([0-9]+[A-Z]*-)').group().strip("-")
                        second_course = re.search(string = d, pattern = '(- [0-9]+[A-Z]*)').group()[2:]

                        refined_data.append(department + " " + first_course)
                        refined_data.append(department + " " + second_course)
                    
                    else:
                        refined_data.append(d)

                else:
                        tmp2 = re.search(string = d, pattern = '([A-Z]{3,} [0-9]+[A-Z]*\–[0-9]+[A-Z]*)')

                        if tmp2 is not None and tmp.group() == tmp2.group():                       
                            department = re.search(string = tmp.group(), pattern = '([A-Z]{3,})').group()
                            first_course = re.search(string = tmp.group(), pattern = '([0-9]+[A-Z]*.*?(?=–))').group().strip("-")
                            second_course = re.search(string = tmp.group(), pattern = '(–[0-9]+[A-Z]*)').group()[1:]
                            
                            print("department:", department, "   first course:", first_course, "    second course:", second_course)

                            # pandas pull from course_data.csv

                            # creating DataFrame from course_data.csv
                            df = pandas.read_csv("data/course_data.csv")
                            mask = (df["department"] == department)
                            result = df.loc[mask]

                            if int(first_course) < 250:


                                for i in range(int(first_course), int(second_course) + 1):
                                    for course_num in result["number"]:
                                        if course_num[:len(first_course)] == str(i):
                                            refined_data.append(department + " " + str(int(first_course) + i))

                            


    driver.close()

    return refined_data

def automate():
    urls = get_urls("backend/web_scraper/result.html")

    majors = dict()

    for url in urls:
        name = get_major_name(url)
        majors[name] = get_requirements_from_url(url)

        print(name, "done!")
        print(majors[name])
    
    return majors




if __name__ == "__main__":
    # x = automate()

    # print("done")
    # print(x)

    print(get_requirements_from_url("/schoolofhumanities/departmentofafricanamericanstudies/africanamericanstudies_ba/"))

    