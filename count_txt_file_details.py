# Python Program to Count Number of Lines, Words and Characters in a .txt File

try:
    file = open("demofile.txt", "r")
    lines = file.readlines()

    # ------------------PRINTING NUMBER OF LINES IN THE TXT FILE

    print("Number Of Lines In 'demofile.txt' = ", len(lines))

    # ------------------CALCULATING NUMBER WORDS IN THE TXT FILE

    words = []
    for i in lines:
        temp_list = i.split()
        for j in temp_list:
            words.append(j)
    print("Number Of Words In 'demofile.txt' = ", len(words))

    # ----------------CALCULATING NUMBER OF CHARACTERS IN THE TXT FILE

    characters = []
    for i in words:
        for j in i:
            characters.append(j)
    print("Number Of Characters In 'demofile.txt' = ", len(characters))

    file.close()

except FileNotFoundError:
    print("File with the entered name not found")
