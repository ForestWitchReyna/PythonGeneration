import sys
from traceback import print_tb

products = ["Bottled Water", "Coke", "Diet Coke", "Coke Zero", "Pepsi", "Lemonade", "Coffee"]

#order = {}#"customer_name", "customer_address", "customer_phone", "status"
order_list = []
status_list = ["preparing", "dispatched", "delivered", "cancelled", "returned", "lost"]

prompt = "\nWhat would you like to do: "    #prompt string so i don't have to type out each case

menu_prompt = "This is the main menu\nHere you can select which option you wish for by typing \
 in the corresponding number for the command \nThe commands are as follows:\n0- Shutdown Program \n1- Product Menu \n2- Order Menu"

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
                    for product in products: 
                        print(product)

                elif command == "2":    #Add new product
                    newProd = input("Please enter the name of the product you wish to add:\n")
                    products.append(newProd)
                    print(f"New product: {newProd} added to product list")

                    for product in products: 
                        print(product)

                elif command == "3":    #List and update products
                    print("Current list of products:")
                    
                    i=0
                    for product in products: #implement as function?
                        print(i,":", product)
                        i+=1

                    while True:
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

                    i=0
                    for product in products: #implement as function?
                        print(i,":", product)
                        i+=1

                elif command == "4":    #Delete product

                    i=0
                    for product in products: #Product list
                        print(i,":", product)
                        i+=1

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

                elif command == "0":    #Back to main menu
                    break                    

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
                    # i=0
                    # for order in order_list: #Order list
                    #     print(i,":", order)
                    #     i+=1
                    
                    orderlist_function()

                    while True:
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
                    # i=0
                    # for status in status_list:
                    #     print (i, ":", status.upper())
                    #     i+=1

                    statuslist_function()

                    while True:
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
                    print("Select which order you would like to update: ")  #leave blank to keep same

                    # i=0
                    # for order in order_list: #Order list
                    #     print(i,":", order)
                    #     i+=1
                    
                    orderlist_function()

                    while True:
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
                    
                    name_input = input("Please enter the new name of the customer placing an order:\n")
                    if name_input != "":
                        order_list[order_index]["customer_name"] = name_input

                    add_input = input("Please enter the new address of the customer placing an order:\n")
                    if add_input != "":
                        order_list[order_index]["customer_address"] = add_input

                    num_input = input("Please enter the new number of the customer placing an order:\n")
                    if num_input != "":
                        order_list[order_index]["customer_number"] = num_input

                    
                    # i=0
                    # for status in status_list: #Status list
                    #     print(i,":", status.upper())
                    #     i+=1

                    statuslist_function()

                    while True:
                        try:
                            status_index = int(input("Please enter the index value of new order status:\n"))
                            print(f"You selected {status_index}- {status_list[status_index]}")
                            if status_index != "":   
                                order_list[order_index]["status"] = status_list[status_index].upper()
                            else:
                                break    

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

                    
                    #order_list[order_index]["status"] = status_list[status_index].upper()

                    #order_list[order_index]["status"] = status_list[0].upper()  #0 to default to "preparing"
                    #order["order_id"] = i 
                    #i += 1
                    #order_list.append(order)

                    print(order)

                elif command == "5":
                    print("Delete existing order")
                    
                    orderlist_function()

                    while True:
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


        else:
            print ("Failure point, main menu loop")     #failure message
    else:
        print("Invalid command, please enter either 0 or 1") #Invalid input message