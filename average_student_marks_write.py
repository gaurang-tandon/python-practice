# Python Program To Read .txt File and Calculate And Write Average Marks Of Each Student
def average_marks(marks):
    add = 0
    for x in marks:
        add += x
    avg = add/(len(marks))
    return round(avg, 2)


try:
    f = open("marks.txt", "r")
    text_in_file = f.readlines()
    for i in text_in_file:
        print(i)
        student = i.split(", ")
        print(student)
        print("\n------------------\n")
        for j in student:
            marks_str = j.strip()
            print(len(marks_str))
            print(len(j))
            # marks_list = (marks_str.split())
            # for k in range(1, len(marks_list)):
            #     marks_list[k] = int(marks_list[k])
            # print(marks_list)




except FileNotFoundError:
    print("File with the entered name not found")
