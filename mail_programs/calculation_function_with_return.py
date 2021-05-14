"""
Python Program to Write a function calculation()
such that it can accept two variables and calculate the addition and subtraction of them.
And also it must return both addition and subtraction in a single return call
"""


def calculation(var_1, var_2):
    sum = var_1 + var_2
    difference = var_1 - var_2
    return [f"Sum of both variables = {sum}", f"Difference of both variables = {difference}"]


result = calculation(5, 3)
for i in result:
    print(i)

