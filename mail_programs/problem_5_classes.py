"""
Define a class which has at least two methods:

getString: to get a string from console input

printString: to print the string in upper case.

Also  include simple test function to test the class methods.
"""


class StringTest:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

        def get_string(self):
            self.fname = input("Enter First Name : ")
            self.lname = input("Enter Last Name : ")
        get_string(self)

    def print_string(self):
        print(self.fname.upper(), "is a", self.gender, "and is", self.age, "years old")


gaurang = StringTest(25, "Male")
gaurang.print_string()
