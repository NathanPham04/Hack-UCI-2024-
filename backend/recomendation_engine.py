from major_class import Course, Professor



def recommend_classes(possible_classes : list[Course]) -> list[Course]:
    sorted_classes = list(sorted(possible_classes, key = lambda x : x.gpa))[:10]

    to_add = []
    to_remove = []
    for i, c in enumerate(sorted_classes):
        if len(c.professors) > 1:
            to_add += Course.duplicate_course(c)
            to_remove.append(i)
    
    for j in reversed(to_remove):
        sorted_classes.pop(j)

    sorted_classes += to_add

    sorted_classes = list(sorted(sorted_classes, key=lambda x : x.get_rating(), reverse=True))
    
    return sorted_classes


if __name__ == "__main__":
    test_classes = [
        Course("TEST 1", "", [], False, [Professor("A", 4.3, 2.1), Professor("D", 1.3, 4.6)], 4.0),   # 12.7
        Course("TEST 2", "", [], False, [Professor("B", 3.3, 2.7)], 3.5),   # 8
        Course("TEST 3", "", [], False, [Professor("C", 2.3, 3.1)], 3.0),   # 3.8
        Course("TEST 4", "", [], False, [Professor("D", 1.3, 4.6)], 2.5),   # -5.3
        Course("TEST 5", "", [], False, [Professor("E", 3.3, 2.3)], 3.7),   # 9
        Course("TEST 6", "", [], False, [Professor("F", 3.7, 2.1)], 4.0)    # 10.9
    ]
    print(recommend_classes(test_classes))