# Task 1 Library System Enhancement: Sharpen your skill sin managin and modifiying data within tuples and lists.
#You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update 
#this system by adding new books and ensuring no duplicates.


def add_book(book, author):                                                                                                   #defining a function that will allow the user to add books to the library
    if (book, author) not in library:                                                                                         #'if' statement set up to check the list for duplicates before appending the list
        library.append((book, author))
        print(f"The book {book} by {author} has been added to the library.")                                                  #'print' statement that tells the user the book has been added to the library
    else:               
        print("A copy of this book already exists in the library.")                                                           #'print' statement telling the user there was a duplicate already in the list



library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley"), ("Calvin and Hobbes", "Bill Watterson")]          # list of tuples, in this case book titles and authors


while True:                                                                                                                   #infinite 'while' loop set up to run through a series of function until the user decides to quit
    print("Welcome to the Library Tracking System. What would you like to do?")                                               #'print statement that welcomes the user
    print("1. View current library\n2. Add book to library\n3. Exit")                                                         #'print' statement that lists the users choices
    choice = input("Please enter your choice (1-3): ")                                                                        # variable chocice set to the user's input to be used in a series of 'if' 'elif' statements 

    if choice == "1":                                                                                                         #begining of the 'if' 'elif' series
        index = 0                                                                                                             #index variable set to 0 to be used in a 'while' loop
        while index < len(library):                                                                                           #'while' loop set to run until the end of the list using len and an index number
            print(f"{library[index][0]} by {library[index][1]}")                                                              #printing off the list for the user in a formatted way using index locations
            index += 1                                                                                                        #counter for the index variable to stop the 'while' loop

    elif choice == "2":                                                                                                       #'elif' statement
        book_input = input("Please Provide the name of the book you would like to add to the library: ")                      #getting a user input and setting it to a variable called book_input
        author_input = input("Please provide the name of the author: ")                                                       #getting a user input and setting it to a variable called author_input
        add_book(book_input, author_input)                                                                                    #calling the function set up earlier using the two user inputs

    elif choice == "3":                                                                                                       #'elif' statement
        print("Thank you for using the Library Tracking System, have a good day.")                                            #'print' statement thanking the user for using the program
        break                                                                                                                 #'break' statement ending the while loop

    else:                                                                                                                     #'else' statement in case an invalid option was entered
        print("Invalid input please enter 1-3")                                                                               #'print' statement telling the user their entry was invalid
 
