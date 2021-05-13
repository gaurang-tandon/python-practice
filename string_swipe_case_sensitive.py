# Python Program To Swipe A String(Case Sensitive) In .txt File

try:
    f = open("demofile2.txt", "r")
    text_in_file = ""
    for i in f.readlines():
        text_in_file += i

    # ------------------ OLD STRING PREVIEW ---------------------- #

    print(text_in_file)

    text_to_replace = input("Enter String too be replaced -> ")
    new_string = input("Enter new String to replace'" + text_to_replace + "' -> ")

    # --------------------- CHANGING STRING ------------------------ #

    for i in range(0, text_in_file.count(text_to_replace)):
        new_text = text_in_file.replace(text_to_replace, new_string)

    # -------------------- NEW CHANGED STRING -----------------------#

    print(new_text)


except FileNotFoundError:
    print("File with the entered name not found")
