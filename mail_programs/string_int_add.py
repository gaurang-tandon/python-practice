# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.


string_input = input("Enter the number -> ")
number_of_repeat = int(input("Enter Number of times to repeat -> "))
string_to_add = ""
addition = 0
for i in range(0, number_of_repeat):
    string_to_add += string_input
    addition += int(string_to_add)

print(addition)
