
# This was an exercise for the Slices module. I was not sure if you could use a variable to put as an index number
# but I found on the internet that I could - so I got it. I have to keep this in mind. My understanding was better
# on this go around.

def sillycase(str):
    first_part = len(str) // 2
    second_part = str[first_part:].upper()
    third_part = str[:first_part].lower()
    return third_part + second_part