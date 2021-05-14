# Python Program to pass variable arguments in a function and print them

def func1(*argvs):
    count = 1
    for i in argvs:
        print("Argument no.", count, ":", i, "is of type :", type(i))
        count += 1


func1(543, "Gaurang", {"name": "tandon"}, [32, 45, "eight"], ("hello", "world"))
