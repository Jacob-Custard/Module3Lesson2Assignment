# Task 1 Customer Order Processing: You are given a list of tuples, each representing a customer's order.
#Each tuple contains the customer;s name, the product ordered, and the quantity. Your task is to unpack
#each tuple and print the order details in a user-friendly format.

def format_orders(orders):                                                                                                     #defining a function to unpack the list of tuples
    for order in orders:                                                                                                       #'for' loop to iterate through the tuples in the list
        name, item, amount = order                                                                                             #unpacking each tuple
        print(f"\nCustomer Order:\n{name} - {item}: {amount}")                                                                 #printing off the tuples in a formatted way


orders_list = [("Alice", "Laptop", 1), ("Bob", "Camera", 2), ("Jake", "flash drive", 5), ("Jess", "Gaming PC", 1)]             #list of tuples


format_orders(orders_list)                                                                                                     #calling the function set up earlier to format the list of tuples
