TICKET_PRICE = 10

tickets_remaining = 100  

# Run this code continuously until we run out of tickets
while tickets_remaining >= 1:

# Output how many tickets are remaining using the tickets_remaining variable

    print("There are {} tickets remaining.".format(tickets_remaining))

    # Gather the user's name and assign it to a new variable
    
    user_name = input("What is your name?  ")
    
    # Prompt the user by name and ask how many tickets they would like
    
    number_of_tickets = input("Hello {}! How many tickets would you like?  ".format(user_name))
    
    # Calculate the price ( number of tickets multiplied by the price ) and assign it to a variable
    
    number_of_tickets = int(number_of_tickets)
    
    customer_price = TICKET_PRICE * number_of_tickets
    
    # Output the price to the screen
    
    print("Your order will cost ${}.".format(customer_price))
    
    # Prompt user if they want to proceed. Y/N?
    
    confirmation = input("Would you like to proceed with your purchase? Y/N:  ")
    
    # If they want to proceed
    
        # Print out the screen "SOLD!" to confirm purchase
        # Gather credit card information and process it.
    if confirmation.lower() == "y":
        print("SOLD! You just purchased {} tickets!".format(number_of_tickets))  
        tickets_remaining -= number_of_tickets
        
        # And then decrement the tickets remaining by the number of tickets purchased
        
    # Otherwise . . . 
    
        #Thank them by name.
    else:
        
        print("Thanks anyway, {}. Maybe next time!".format(user_name))
    
# Notify the user that the tickets are sold out

print("Tickets are now sold out : )")
