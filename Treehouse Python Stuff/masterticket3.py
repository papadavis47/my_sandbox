TICKET_PRICE = 10

tickets_remaining = 100  

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    user_name = input("What is your name?  ")
    number_of_tickets = input("Hello {}! How many tickets would you like?  ".format(user_name))
    # Expect a ValueError to happen and handle it appropriately . . . remember to test it out!
    try:
        number_of_tickets = int(number_of_tickets)
        # Raise a ValueError if the request is for more tickets than are available
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        # Include the error text in the output
        print("Sorry. That is not valid number of tickets. {}. Please try again.".format(err))
    else:
        customer_price = TICKET_PRICE * number_of_tickets
        print("Your order will cost ${}.".format(customer_price))
        confirmation = input("Would you like to proceed with your purchase? Y/N:  ")
        if confirmation.lower() == "y":
            #ToDo Gather credit card information and process it.
            print("SOLD! You just purchased {} tickets!".format(number_of_tickets))  
            tickets_remaining -= number_of_tickets
        else:
            print("Thanks anyway, {}. Maybe next time!".format(user_name))
print("Tickets are now sold out : )")
