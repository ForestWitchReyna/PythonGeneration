import sys
import csv
from traceback import print_tb

products = ["Bottled Water", "Coke", "Diet Coke", "Coke Zero", "Pepsi", "Lemonade", "Coffee"]

#order = {}#"customer_name", "customer_address", "customer_phone", "status"
order_list = []
courier_list = ["Royal Mail", "DPD", "Parcel Force"]
status_list = ["PREPARING", "DISPATCHED", "DELIVERED", "CANCELLED", "RETURNED", "LOST"]

prompt = "\nWhat would you like to do: "    #prompt string so i don't have to type out each case

menu_prompt = "This is the main menu\nHere you can select which option you wish for by typing \
    in the corresponding number for the command \nThe commands are as follows:\n0- Shutdown Program \n1- Product Menu \n2- Order Menu \
    \n3- Courier Menu"

#move menu stuff into functions

def list_orders():
    i=0
    for order in order_list: #Order list
        print(i,":", order)
        i+=1
    return i

def list_status():
    i=0
    for status in status_list: #Status list
        print(i,":", status)
        i+=1
    return i

def list_products():
    i=0
    for product in products: #implement as function?
        print(i,":", product)
        i+=1
    return i

def list_couriers():
    i=0
    for courier in courier_list: #courier list
        print(i, ":", courier)
        i+=1
    return i

def load_products():
    return

def load_couriers():
    return

def validate_input(inputContainer):
    #pass in lists and dictionaries as inputContainer

    while True: #input validation loop
        try:
            listIndex = input()
            if listIndex == "":
                break
            listIndex = int(listIndex)
            print(f"You selected {listIndex}- {inputContainer[listIndex]}")                           
        except ValueError:
            print ("Invalid command, please enter an existing index value")
            continue
        except IndexError:
            print ("That was not an existing index value")
            continue
        else:
            break
    return listIndex


def add_products(): #add products function
    while True:
        newProd = input("Please enter the name of the product you wish to add:\n")
        if newProd == "":
            break
        products.append(newProd)
        print(f"New product: {newProd} added to product list")
        list_products()
    return


def update_products(): #update products function
    while True:
        print("Current list of products:")
        list_products()

        print("\nPlease enter the index value of the product you wish to update, " \
            "or leave blank to back out:\n") 

        product_index = validate_input(products) #input validation function

        if product_index == "":
            print("Returning to product menu")  #backs out to product menu
            break

        updProd = input("Please enter the new name for the product you wish to update:\n")
    
        products[product_index] = updProd
        list_products()
    return


def delete_products(): #delete product function
    while True:
        list_products()
        print("\nPlease enter the index value of the product you wish to remove," \
            "or leave blank to back out:\n") 
                
        product_index = validate_input(products) #input validation function

        if product_index == "":
            print("Returning to product menu")  #backs out to product menu
            break

        print(f"{products[product_index]} has been deleted.")  #Show whats being deleted
        products.pop(product_index)
    return


def add_orders(): #add order function
    order = {}
    print("Create new order")   #creates a new order dict (add checks for validity)
    order["customer_name"] = input("Please enter the name of the customer placing an order:\n")
    order["customer_address"] = input("Please enter the address of the customer placing an order\n")
    order["customer_number"] = input("Please enter the phone number of the customer placing an order\n")
    
    list_couriers()

    courier_index = validate_input(courier_list) #input validation function
    order["courier"] = courier_list[courier_index]
    order["status"] = status_list[0]  #0 to default to "preparing"
    order_list.append(order)

    print(order)
    return


def update_status(): #update order status function
    print("Update existing order status")
            
    while True:

        list_orders()

        print("\nPlease enter the index value of the order you wish to update the status of, " \
            "or leave blank to back out:\n") 

        order_index = validate_input(order_list) #input validation function
        if order_index == "":
            print("Returning to order menu")  #backs out to order menu
            break

        list_status()

        print("\nPlease enter the index value of the new order status," \
            "or leave blank to back out:\n") 
    
        status_index = validate_input(status_list) #input validation function
        if status_index == "":
            print("Returning to order menu")  #backs out to order menu
            break

        order_list[order_index]["status"] = status_list[status_index]

        print(order_list[order_index])
    return


def update_orders(): #update order function
    while True:                
        list_orders()

        print("\nPlease enter the index value of the order you wish to update, " \
            "or leave blank to back out:\n") 
    
        order_index = validate_input(order_list) #input validation function
        if order_index == "":
            print("Returning to order menu")  #backs out to order menu
            break

        print("Leave the following inputs blank to keep unchanged")
        
        name_input = input("Please enter the new name of the customer placing an order:\n")
        if name_input != "":
            order_list[order_index]["customer_name"] = name_input

        add_input = input("Please enter the new address of the customer placing an order:\n")
        if add_input != "":
            order_list[order_index]["customer_address"] = add_input

        num_input = input("Please enter the new number of the customer placing an order:\n")
        if num_input != "":
            order_list[order_index]["customer_number"] = num_input

        list_status()
        
        print("\nPlease enter the index value of the new order status") 
    
        status_index = validate_input(status_list) #input validation function
        if status_index != "":
            order_list[order_index]["status"] = status_list[status_index]

        print(order_list[order_index])
    return

def delete_orders(): #delete order function
    while True:
        print("Delete existing order")
        list_orders()

        print("\nPlease enter the index value of the order you wish to delete, " \
            "or leave blank to back out:\n") 
    
        order_index = validate_input(order_list) #input validation function
        if order_index == "":
            print("Returning to order menu")  #backs out to order menu
            break

        print(f"{order_list[order_index]} has been deleted.")  
        order_list.pop(order_index)
        break
    return

def add_courier(): #add courier function
    while True:
        new_courier = input("Please enter the name of the courier you wish to add, or leave blank to back out:\n")
        if new_courier == "":
            break
        courier_list.append(new_courier)
        print(f"New courier: {new_courier} added to courier list")
        list_couriers()
    return

def update_courier(): #update courier function
    while True:
        print("Current list of couriers:")
        list_couriers()

        print("\nPlease enter the index value of the courier you wish to update, " \
            "or leave blank to back out:\n") 

        courier_index = validate_input(courier_list) #input validation function

        if courier_index == "":
            print("Returning to courier menu")  #backs out to courier menu
            break

        upd_courier = input("Please enter the new name for the courier you wish to update:\n")
    
        courier_list[courier_index] = upd_courier
        list_couriers()
    return

def delete_courier(): #delete courier function
    while True:
        list_couriers()
        print("\nPlease enter the index value of the courier you wish to remove," \
            "or leave blank to back out:\n") 
                
        courier_index = validate_input(courier_list) #input validation function

        if courier_index == "":
            print("Returning to courier menu")  #backs out to courier menu
            break

        print(f"{courier_list[courier_index]} has been deleted.")  #Show whats being deleted
        courier_list.pop(courier_index)
    return

while True: #main menu loop
    print(menu_prompt)
    command = input(prompt)

    if command == "0":      
        sys.exit("Shutting down program")       #shutdown command

    elif command == "1":    #product menu command
        subMenu = "\n0- Return to main menu \n1- Print product list \n2- Create new product \
            \n3- Update existing product \n4- delete an existing product"
        
        while True:
            print(subMenu)
            command = input(prompt) #product menu loop
            if command == "0":
                print("returning to main menu")
                break

            elif command == "1":    #Product list
                print("Products we have are:\n")
                list_products()

            elif command == "2":    #Add new product
                add_products()

            elif command == "3":    #List and update products
                update_products()

            elif command == "4":    #Delete product
                delete_products()
                                    
            else:
                print("Invalid Command: Please enter a valid index number")


    elif command == "2":    #Order menu command
        ord_menu = "This is the order menu\n0- Return to main menu \n1- Print orders dictionary \n2- Create new order\
            \n3- Update existing order status \n4- Update an existing order \n5- Delete an existing order"

        while True:
            print(ord_menu)
            command = input(prompt) 

            if command == "0":  #return to main menu
                print("returning to main menu")
                break

            elif command == "1": #Print all existing orders
                print("This is a list of all existing orders:")
                for order in order_list:
                    print(order)

            elif command == "2": #create a new order
                add_orders()

            elif command == "3": #Update an existing order status
                update_status()
                    

            elif command == "4": #Update an existing order
                update_orders()

            elif command == "5": #Delete an existing order           
                delete_orders()
    

    elif command == "3":
        courier_menu = "This is the courier menu\n0- Return to main menu \n1- Print list of couriers \n2- Create new courier\
            \n3- Update existing courier \n4- Delete an existing courier"

        while True:
            print(courier_menu) #Courier menu
            command = input(prompt)
            if command == "0":
                print("returning to main menu")
                break

            elif command == "1": #Print couriers list
                print("This is a list of couriers used")
                list_couriers()

            elif command == "2": #add new courier
                add_courier()

            elif command == "3": #Update existing courier
                update_courier()

            elif command == "4": #Delete existing courier
                delete_courier()


    else:
        print ("Failure point, main menu loop")     #failure message
