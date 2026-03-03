"""
perform file operations we can use file operations like open
# open
# write
# read
.txt, .png, .jpg, .xlsx, .csv, .json
"""
"""
r: read, it will be used to read the data from the file, if file is not exists it will through FileNotFoundError
w: write, if file is exists it will override the data, if not exists it will create a new file
a: append, if file is already exists it will append the data,if file is not exists it will create a file
r+: read and write: If file is not there, it will raise exception
w+: write and read: it will create a file, it will override data
a+:
wb:
rb:
ab:

open(filename, mode)
Whenever we use open method to file operations, we have to close the close explicitly by using close method.
"""

# obj = open("file1.txt", "w")
# obj.write("Hello world, welcome to msn python automation testing\n")
# obj.writelines(["hello I am learning python\n", "Hello I am learning python automation\n", "I am learning at msn python\n"])

# print(obj.closed)
# obj.close()
# print(obj.closed)

# write a function to read a file data

"""
write: we can write the data into a file
writelines: we can write multiple lines into a file
read: it will read the data into a single string
readline: it will read only one line at once
readlines: it will read data into a list of lines
"""


def read_data_from_file(filename, mode):
    try:
        obj = open(filename, mode)
        if mode == "r":
            data = obj.read() #
            print(data)
            print(obj.readline()) # it will read single line at once
            print(obj.readlines()) # list of lines

    except FileNotFoundError as e:
        print("File not found, please try to create a file by using w mode")


# read_data_from_file("file1.txt", "r")

# obj = open("file2.txt", "a")
# obj.write("hello this is append mode file operations\n")
# obj.close()

"""
with open(filename, mode) as rd:
    rd.read()

with open is context manager, no need to close the explicitly
"""
# with open("file1.txt", "r") as rd:
#     print(rd.read())
#
#
# print(rd.closed)

# tell(): it will return cursor position
# seek: we can set the cursor position
# with open("file3.txt", "w+") as wr:
#     wr.write("hello")
#     print('current cursor:', wr.tell())
#     wr.seek(2)
#     print(wr.read())
# print(dir(wr))

with open("file3.txt", "r+") as wr:
    print(wr.read())
    # print('current cursor:', wr.tell())
    # wr.seek(2)
    print(wr.write("hey I am writing new story"))
# print(dir(wr))
