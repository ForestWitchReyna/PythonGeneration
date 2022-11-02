import csv

filename = "testdata.csv"


#read file

# with open(filename) as file:
#     reader = csv.reader(file, delimiter=",")
#     for row in reader:
#         print(row)



#read file as Dict

# with open(filename) as file:
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         print(row)

#defaults to comma as delimiter

#write file as csv

# with open("people.csv", mode='w') as file:
#     writer = csv.writer(file, delimiter=",")

#     writer.writerow(["name","surname","age"])
#     writer.writerow(["Lydia","Miller","27"])





#write file as csv dictionary
people = [
    {
        "name": "Lydia",
        "surname": "Miller",
        "age": 27
    },
    {
        "name": "Test",
        "surname": "McTest",
        "age": "55"
    }
]

# for person in people:
#     print(person["surname"])

with open("people_dict.csv", mode='w') as file:
    fieldnames = ["name","surname","age"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for person in people:
        writer.writerow(person)



    # writer.writerow(["name","surname","age"])
    # writer.writerow(["Lydia","Miller","27"])