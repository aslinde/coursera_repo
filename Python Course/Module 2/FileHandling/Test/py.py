import os
print(os.getcwd())

file = open("C:/Users/estu0/OneDrive/Documents/VScode_code/Coursera/Python Course/Module 2/FileHandling/file.txt", mode="r") #You need to include the actual file
#file = open("file.txt", mode="r")
print(file.readline())

file.close()

with open("C:/Users/estu0/OneDrive/Documents/VScode_code/Coursera/Python Course/Module 2/FileHandling/file.txt", mode="r") as files:
    print(files.readlines())