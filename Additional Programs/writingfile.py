people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

with open ("new_people.txt", "w") as file:
        for person in people:
            file.write(f"{person}\n")


# try:
#     file = open ("new_people.txt", "w")
#     for person in people:
#         file.write(f"{person}\n")

# except FileNotFoundError as fnfe:
#     print("Unable to open file: " + str(fnfe))

# finally:
#     file.close()