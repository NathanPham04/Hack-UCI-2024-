from major_class import Course


def recommend_classes(possible_classes : list[Course]) -> list[Course]:
    sorted_classes = list(sorted(possible_classes, key = lambda x : x.gpa))[:10]

    to_add = []
    to_remove = []
    for i, c in enumerate(sorted_classes):
        if len(c.professors) > 1:
            to_add.add(Course.duplicate(c))
            to_remove.append(i)
    
    for j in reversed(to_remove):
        sorted_classes.pop(j)

    sorted_classes += to_add

    sorted_classes = list(sorted(sorted_classes, key=lambda x : x.get_rating(), reverse=True))
    
    return sorted_classes