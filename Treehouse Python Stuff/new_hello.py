
# This is some very basic stuff from Treehouse Python basics course. Something simple about conditional statements.
# It feels like I am finally starting to get it in my head. Feeling more comfortable with it now.

first_name = input("What is your first name?  ")
print("Hello,", first_name)
if first_name == "John":
    print(first_name, "is learning Python.")
elif first_name == "Diego": # Decided to try an inline code comment here. Experimenting.
    print("{} is John Davis' son. He will learn Python when he and his dad buy a Raspberry Pi!\nand work on it together:)".format(first_name))
else:
    print("You should totally learn Python, {}!".format(first_name))
print("Have a great day, {}!".format(first_name))
