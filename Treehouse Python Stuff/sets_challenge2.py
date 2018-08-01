


COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(set_of_topics):
    overlap = []
    for key, value in COURSES.items():
        if value.intersection(set_of_topics):
            overlap.append(key)
    return overlap

# This was a new one. Using a different set method than the one above. I needed some help from the web but once I remembered
# how to loop over a dictionary - I was allright.
def covers_all(set_of_topics):
    all_covered = []
    for key, value in COURSES.items():
        if value.issuperset(set_of_topics):
            all_covered.append(key)
    return all_covered
    
    
    