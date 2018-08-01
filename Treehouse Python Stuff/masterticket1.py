# I will try to make this my own in some way. 7/18/2018

TICKET_PRICE = 10

tickets_remaining = 100  

# Output how many tickets are remaining using the tickets_remaining variable

print("There are {} tickets remaining.".format(tickets_remaining))

# Gather the user's name and assign it to a new variable

user_name = input("What is your name?  ")

# Prompt the user by name and ask how many tickets they would like

# Calculate the price ( number of tickets multiplied by the price ) and assign it to a variable

# Output the price to the screen
number_of_tickets = input("Hello {}! How many tickets would you like?  ".format(user_name))
number_of_tickets = int(number_of_tickets)

customer_price = TICKET_PRICE * number_of_tickets

print("Your order will cost ${}.".format(customer_price))