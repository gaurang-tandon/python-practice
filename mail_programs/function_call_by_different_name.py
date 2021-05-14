# Assign a different name to function and call it through the new name

def func1(arg):
    print(arg)


def func2(func):
    func1(func)
    func1(func.upper())


def func3(argv):
    func1(argv)
    func1(argv.swapcase())


func1("Hello World!")
func2("My Name Is Gaurang Tandon")
func3("This Is A python Program")
