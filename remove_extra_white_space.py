# Python Program to remove extra white spaces in a .text file

try:
    f = open("demofile.txt", "r")
    file_text = f.readlines()
    new_text = ""

    for i in file_text:
        # SPLITTING ONE ELEMENT INTO MANY

        file_elements = i.split()

        # JOINING MANY INTO ONE

        seperator = ' '
        without_space_text = seperator.join(file_elements)

        # JOINING ELEMENTS TO A STRING
        new_text += without_space_text

    f.close()

    # WRITING TEXT INTO NEW FILE

    create_new_file = open("new file without spaces", "x")
    if create_new_file:
        new_file = open("new file without spaces", "w")
        new_file.write(new_text)
        new_file.close()
    create_new_file.close()

    print("New File text file without extra white spaces created")

except FileExistsError:
    print("""GIVEN NEW FILE NAME ALREADY EXISTS.
New txt file cannot be created with same name.
Delete The File Then Try Again
""")
except FileNotFoundError:
    print("File with the entered name not found")
