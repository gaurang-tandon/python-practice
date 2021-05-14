# Write a program that accepts a comma separated sequence of words as input
# and prints the words in a comma-separated sequence after sorting them alphabetically.

def string_sort(argv):
    list1 = argv.split(",")
    list1.sort()
    # print(list1)
    sorted_string = ",".join(list1)
    return sorted_string


string = string_sort("without,hello,bag,world")
print(string)
