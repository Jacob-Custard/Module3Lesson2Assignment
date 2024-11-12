# Task 1 Formatting Flight Itineraries: Create a python function tht takes a list of tuples as an argument.
#Each tuple contains infomation about a flight itinerary: (travler_name, origin, destination). The function 
#should foramt and rerturn a string that lists each itinerary.

def format_itineraries(itineraries):                                                                                                                                   #defining a function to format the itineraries                                                                                        
    index = 0                                                                                                                                                          #setting a variable called "index" to 0 to use in a while loop
    while index < len(itineraries):                                                                                                                                    #'while' loop that whill keep cycling through a list of variable length using 'index' variable set up earlier
        print(f"Itinerary {index + 1}: {itineraries[index][0]} - From {itineraries[index][1]} to {itineraries[index][2]}")                                             #'print' statement to display the tuples in the list in a formatted way using index positions
        index += 1                                                                                                                                                     #'index' counter to make sure the loop doesn't become an infinite loop


list_of_itineraries = [("Sal", "Denver", "Seoul"), ("Matt", "Memphis", "Dallas"), ("Jess", "Orlando", "London"), ("Lesli", "Charleston", "Las Vegas")]                 #list of tuples


format_itineraries(list_of_itineraries)                                                                                                                                #calling the funciton format_itineraries