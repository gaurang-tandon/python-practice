# Python Program To Swipe A String In .txt File

try:
    f = open("demofile2.txt", "r")
    text_in_file = ""
    for i in f.readlines():
        text_in_file += i

    # ------------------ OLD STRING PREVIEW ---------------------- #

    print(text_in_file)

    text_to_replace = input("Enter String too be replaced -> ")
    new_string = input("Enter new String to replace '" + text_to_replace + "' -> ")

    # -------------- MAKING STRINGS CASE INSENSITIVE ----------------#

    x1 = text_to_replace.lower()
    x2 = text_to_replace.title()
    x3 = text_to_replace.upper()

    # ------ COUNTING OCCURRENCE OF STRING IRRESPECTIVE OF CASE -----#

    count1 = text_in_file.count(x1)
    count2 = text_in_file.count(x2)
    count3 = text_in_file.count(x3)

    # --------------------- CHANGING STRING ------------------------ #

    for i in range(0, count1):
        new_text = text_in_file.replace(x1, new_string)

    for i in range(0, count2):
        new_text = new_text.replace(x2, new_string)

    for i in range(0, count3):
        new_text = new_text.replace(x3, new_string)

    # -------------------- NEW CHANGED STRING -----------------------#

    print(new_text)

except FileNotFoundError:
    print("File with the entered name not found")
