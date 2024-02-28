class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

# Create an instance of the Person class
bob = Person("Bob", 30)

# Use the greet method
print(bob.greet())

#updated check line 15