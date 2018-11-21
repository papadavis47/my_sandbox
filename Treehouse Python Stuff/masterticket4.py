TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100 
# Create the calculate_price function. It takes the number_of_tickets and returns
# TICKET_PRICE * number_of_tickets
def calculate_price(number_of_tickets):
    return (TICKET_PRICE * number_of_tickets) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    user_name = input("What is your name?  ")
    number_of_tickets = input("Hello {}! How many tickets would you like?  ".format(user_name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Sorry. That is not valid number of tickets. {}. Please try again.".format(err))
    else:
        customer_price = calculate_price(number_of_tickets)
        print("Your order will cost ${}.".format(customer_price))
        confirmation = input("Would you like to proceed with your purchase? Y/N:  ")
        if confirmation.lower() == "y":
            #ToDo Gather credit card information and process it.
            print("SOLD! You just purchased {} tickets!".format(number_of_tickets))  
            tickets_remaining -= number_of_tickets
        else:
            print("Thanks anyway, {}. Maybe next time!".format(user_name))
print("Tickets are now sold out : )")
