
# I want to remember the .values(), .keys(), and .items() methods for working with dictionaries in Python.
def num_teachers(dict):
    num = 0
    for key in dict.keys():
        num += 1
    return num

def num_courses(dict):
    list = []
    for value in dict.values():
        list.extend(value)
    return len(list)

def courses(dict):
    list = []
    for value in dict.values():
        list.extend(value)
    return list

def most_courses(dict):
    max_count = 0
    champion = ""
    for teacher, courses in dict.items():
        if len(courses) > max_count:
            max_count = len(courses)
            champion = teacher
    return champion

# The fifth task is a different one than before. I spent a long time working on this challenge. Frustrating. I should have taken a break. 
# I had a problem with the browser, I guess. The code was good, but it wasn't passing because of some browser/website problem.

def stats(dict):
    master_list = []
    for teacher, courses in dict.items():
        inside_list = [teacher, len(courses)]
        master_list.append(inside_list)
    return master_list