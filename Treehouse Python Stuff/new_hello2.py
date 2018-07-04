
# 2nd version with an added conditional statement

first_name = input("What is your first name?  ")
print("Hello,", first_name)
if first_name == "John":
    print(first_name, "is learning Python.")
elif first_name == "Diego":
    print("{} is John Davis' son. He will learn Python when he and his dad buy a Raspberry Pi!\nand work on it together:)".format(first_name))
else: # This is just incase we have a younger user who can't yet read.
    age = int(input("How old are you?  "))
    if age <= 6:
        print("Wow, you are {}. If you are confident in your reading ability . . . ".format(age))
    print("You should totally learn Python, {}!".format(first_name))
print("Have a great day, {}!".format(first_name))
