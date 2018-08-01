# This code is from a code challenge in Treehouse List course. It is meant tacos_only
# illustrate the importance of making copies of lists before iterating.

all_restaurants = [
    "Taco City",
    "Burgertown",
    "Tacovilla",
    "Hotdog station",
    "House of tacos",
]

def tacos_only(restaurants):
    taco_joints = restaurants.copy()
    for taco_joint in taco_joints.copy():
        if "taco" not in taco_joint.lower():
            taco_joints.remove(taco_joint)
    return taco_joints

dinner_options = tacos_only(all_restaurants)