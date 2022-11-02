# create a new object called Person
class Person:
# Constructor
    def __init__(self, name, age):

# Properties
        self.name = name
        self.age = age

# Method
    def increment_age(self):
        self.age += 1
    def introduce_yourself(self):
        print(f"Hello my name is {self.name}, I am {self.age} years old.")
        
john = Person('John', 10) # is an object of type `Person`

# properties(props) and methods using dot notation
john.age # 10
john.increment_age()
john.age # 11