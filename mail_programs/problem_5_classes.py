"""
Define a class which has at least two methods:

getString: to get a string from console input

printString: to print the string in upper case.

Also  include simple test function to test the class methods.
"""


class StringTest:
    def __init__(self, number, age, gender):
        self.number = number
        self.age = age
        self.gender = gender

        def get_string():
            self.fname = input(f"Enter First Name of {self.number} person : ")
            self.lname = input("Enter Last Name : ")

        get_string()

    def print_string(self):
        print(f"{self.fname} {self.lname} is a {self.gender} and is {self.age} years old".upper())


object_1 = StringTest(1, 25, "Male")
object_2 = StringTest(2, 24, "Female")
object_3 = StringTest(3, 26, "Male")

object_1.print_string()
object_2.print_string()
object_3.print_string()

