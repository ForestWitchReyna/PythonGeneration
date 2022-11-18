import sys
from traceback import print_tb

products = ["Bottled Water", "Coke", "Diet Coke", "Coke Zero", "Pepsi", "Lemonade", "Coffee"]

#order = {}#"customer_name", "customer_address", "customer_phone", "status"
order_list = []
courier_list = []
status_list = ["preparing", "dispatched", "delivered", "cancelled", "returned", "lost"]

prompt = "\nWhat would you like to do: "    #prompt string so i don't have to type out each case

menu_prompt = "This is the main menu\nHere you can select which option you wish for by typing \
 in the corresponding number for the command \nThe commands are as follows:\n0- Shutdown Program \n1- Product Menu \n2- Order Menu"

#Tech debt goals:
#make function for input validation loops
#make function for 


def orderlist_function():
    i=0
    for order in order_list: #Order list
        print(i,":", order)
        i+=1
    return i

def statuslist_function():
    i=0
    for status in status_list: #Status list
        print(i,":", status.upper())
        i+=1
    return i

def productlist_function():
    i=0
    for product in products: #implement as function?
        print(i,":", product)
        i+=1
    return i

def input_validation_function(inputIndex, inputContainer):

    #pass in input as inputIndex and return as validIndex
    #pass in lists and dictionaries as inputContainer and , assign to relevant variables

    while True: #input validation loop
        try:
            validIndex = int(inputIndex)
            #implement as function?

            print(f"You selected {validIndex}- {inputContainer[validIndex]}")                           
        except ValueError:
            print ("Invalid command, please enter an existing index value")
            continue
        except IndexError:
            print ("That was not an existing index value")
            continue
        else:
            break

while True: #main menu loop
    print(menu_prompt)
    command = input(prompt)

    if command in ["0", "1", "2"]:
        if command == "0":      
            sys.exit("Shutting down program")       #shutdown command

        elif command == "1":    #product menu command
            subMenu = "\n0- Return to main menu \n1- Print product list \n2- Create new product \
                \n3- Update existing product \n4- delete an existing product"
            print(subMenu)
            while True:
                command = input(prompt) #product menu loop
                if command == "0":
                    print("returning to main menu")
                    break

                elif command == "1":    #Product list
                    print("Products we have are:\n")
                    productlist_function()

                elif command == "2":    #Add new product
                    newProd = input("Please enter the name of the product you wish to add:\n")
                    products.append(newProd)
                    print(f"New product: {newProd} added to product list")
                    productlist_function()

                elif command == "3":    #List and update products
                    print("Current list of products:")
                    productlist_function()

                    while True: #input validation loop
                        try:
                            prodIndex = int(input("Please enter the index value of the product you wish to update:\n"))
                            #implement as function?

                            print(f"You selected {prodIndex}- {products[prodIndex]}")                           
                        except ValueError:
                            print ("Invalid command, please enter an existing index value")
                            continue
                        except IndexError:
                            print ("That was not an existing index value")
                            continue
                        else:
                            break

                    updProd = input("Please enter the new name for the product you wish to update:\n")

                    products[prodIndex] = updProd
                    productlist_function()

                elif command == "4":    #Delete product

                    productlist_function()

                    while True:
                        try:
                            prodIndex = int(input("Please enter the index value of the product you wish to remove:\n"))
                            #products[prodIndex]
                            print(f"You selected {prodIndex}- {products[prodIndex]}")                           
                        except ValueError:
                            print ("Invalid command, please enter an existing index value")
                            continue
                        except IndexError:
                            print ("That was not an existing index value")
                            continue
                        else:
                            break
                        
                    products.pop(prodIndex)                   

                else:
                    print("Invalid command- product menu failure")
                    print(subMenu)


        elif command == "2":
            ord_menu = "This is the order menu\n0- Return to main menu \n1- Print orders dictionary \n2- Create new order\
                \n3- Update existing order status \n4- Update an existing order \n5- Delete an existing order"

            while True:
                print(ord_menu)
                command = input(prompt) #product menu loop
                if command == "0":
                    print("returning to main menu")
                    break
                elif command == "1":
                    print("This is a list of all existing orders:")
                    print(order_list)

                    for order in order_list:
                        print(order)

                elif command == "2":
                    order = {}
                    print("Create new order")   #creates a new order dict (add checks for validity)
                    order["customer_name"] = input("Please enter the name of the customer placing an order:\n")
                    order["customer_address"] = input("Please enter the address of the customer placing an order\n")
                    order["customer_number"] = input("Please enter the phone number of the customer placing an order\n")
                    order["status"] = status_list[0].upper()  #0 to default to "preparing"
                    #order["order_id"] = i 
                    #i += 1
                    order_list.append(order)

                    print(order)
                    #print(order_list)

                elif command == "3":
                    print("Update existing order status")
                    orderlist_function()

                    while True: #input validation loop
                        try:
                            order_index = int(input("Please enter the index value of the order you wish to update:\n")) #implement as function?
                            print(f"You selected {order_index}- {order_list[order_index]}")  

                        except ValueError:
                            print ("Invalid command, please enter an existing index value")
                            continue

                        except IndexError:
                            print ("That was not an existing index value")
                            continue

                        else:
                            break

                    statuslist_function()

                    while True: #input validaiton loop
                        try:
                            status_index = int(input("Please enter the index value of new order status:\n"))
                            print(f"You selected {status_index}- {status_list[status_index].upper()}\n")    

                        except ValueError:
                            print ("Invalid command, please enter an existing index value")
                            continue

                        except IndexError:
                            print ("That was not an existing index value")
                            continue

                        else:
                            break

                    order_list[order_index]["status"] = status_list[status_index].upper()

                    print(order_list[order_index])

                    #make status list, add option for "other: user input"

                elif command == "4":

                    while command == "4": #new command loop, maybe True then break, exit on blank input
                        print("Select which order you would like to update: ")  #leave blank to keep same
                        
                        orderlist_function()

                        #order_input = input("Please enter the index value of the order you wish to update:\n")
                        #if order_input == "":
                        #    break

                        while True:
                            try:
                                order_input = input("Please enter the index value of the order you wish to update:\n") #implement as function?
                                
                                #Change input to string input, then use try catch for converting to int, with no entry resulting in backing out
                                #Once fixed and working, add as function, maybe add blank input as menu refresh on menus
                                #Possible fix- change menu if statements to while loops, have command == "" operate as the main menus so changing to blank
                                #will back out to menu
                                #tab everything to fall under above loop?

                                if order_input == "":   
                                    print("Backing out")
                                    command = "1"
                                    break
                                else:
                                    order_index = int(order_input)                                
                                    print(f"You selected {order_index}- {order_list[order_index]}")                           
                            except ValueError:
                                print ("Invalid command, please enter an existing index value")
                                continue
                            
                            except IndexError:
                                print ("That was not an existing index value")
                                continue
                            else:
                                break

                        if command == "1":
                            break

                        name_input = input("Please enter the new name of the customer placing an order:\n")
                        if name_input != "":
                            order_list[order_index]["customer_name"] = name_input

                        add_input = input("Please enter the new address of the customer placing an order:\n")
                        if add_input != "":
                            order_list[order_index]["customer_address"] = add_input

                        num_input = input("Please enter the new number of the customer placing an order:\n")
                        if num_input != "":
                            order_list[order_index]["customer_number"] = num_input

                        statuslist_function()

                        while True: #Input validation loop
                            try:
                                status_index = int(input("Please enter the index value of new order status:\n"))
                                print(f"You selected {status_index}- {status_list[status_index]}")
                                if status_index != "":   
                                    order_list[order_index]["status"] = status_list[status_index].upper()
                                else:
                                    print("Backing out")
                                    continue    

                            except ValueError:
                                print ("Invalid command, please enter an existing index value")
                                continue

                            except IndexError:
                                print ("That was not an existing index value")
                                continue

                            else:
                                break

                        
                        # order_list[order_index]["customer_name"] = input("Please enter the name of the customer placing an order:\n")
                        # order_list[order_index]["customer_address"] = input("Please enter the address of the customer placing an order\n")
                        # order_list[order_index]["customer_number"] = input("Please enter the phone number of the customer placing an order\n")

                        #cha
                        #order_list[order_index]["status"] = status_list[status_index].upper()

                        #order_list[order_index]["status"] = status_list[0].upper()  #0 to default to "preparing"
                        #order["order_id"] = i 
                        #i += 1
                        #order_list.append(order)

                        print(order)

                elif command == "5":
                    print("Delete existing order")
                    
                    orderlist_function()

                    while True: #Input validation loop
                        try:
                            order_index = int(input("Please enter the index value of the order you wish to delete:\n")) #implement as function?
                            print(f"You selected {order_index}- {order_list[order_index]}")

                        except ValueError:
                            print ("Invalid command, please enter an existing index value")
                            continue

                        except IndexError:
                            print ("That was not an existing index value")
                            continue
                        else:
                            break

                    order_list.pop(order_index)
        
        elif command == "3":
            print("Couriers Menu:")

        else:
            print ("Failure point, main menu loop")     #failure message
    else:
        print("Invalid command, please enter either 0 or 1") #Invalid input message