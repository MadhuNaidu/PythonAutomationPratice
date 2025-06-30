# open() by using open method we can perform file operations
# with open() by this method we can perform file operations
"""
file modes:
w: write-> if file is not there it will create the file and write the data,
 if already file exists it will override the data
r: read: -> if file exists it will read the data otherwise it will through exception like FileNotFoundError
a: append -> it will append the data at the end of the file.
w+: write and read: -> if file is not there it will create the file,
if file is there it will override data and we can read data from file
r+: read and write: We can read and write but we cannot create new file if file not exist
a+: We can read, write and create new file if file not exists.

wb:
rb:
ab:
wb+:
rb+:
"""
# write: it will write a single line.
# writelines: we can write multiple lines.
# read: it will read all the data into a single str
# readline: it will read only one line at once
# readlines: it will read all the lines and it will return a list of lines
"""
# obj = open("demo.txt", "w")
obj = open("C:\\Users\madhusudhana_naidu\PycharmProjects\python_practice\demo.txt", "w")
obj.write("Hello I am learning file handling concept first line.\n")
obj.write("Hello I am learning file handling concept second line.\n")
obj.writelines(["third line\n", "fourth line\n", "fivth line\n"])
# obj.close()
"""


def write_file_with_data(filename, mode):
    try:
        obj = open(filename, mode)
        obj.write("Learning file handlings along with exception handling mechanism.")
    except PermissionError as e:
        print("got the exception:", e)
    except FileNotFoundError as e:
        print("Got the exception:", e)
    finally:
        obj.close()


# write_file_with_data("learn.txt", "w")


def file_operations(filepath, mode):
    try:
        if mode == "w":
            obj = open(filepath, mode)
            obj.write("Helllo file with write mode1\n")
            obj.write("Helllo file with write mode2\n")
            obj.write("Helllo file with write mode3\n")
            obj.write("Helllo file with write mode4\n")
            obj.write("Helllo file with write mode5\n")
        elif mode == "r":
            # import os
            # if os.path.exists(filepath):
            obj = open(filepath, mode)
            # print(obj.read()) # it will read all the data from the buffer
            # print(data.count("Helllo"))
            print(obj.readlines())
            print(obj.readline())
    except FileNotFoundError as e:
        print("Got the exception:", e)

    finally:
        obj.close()


# file_operations("demo1.txt", "w")
# file_operations("demo1.txt", "r")
# find specific word count in a file?

# with open("demo.txt", "r") as rd:
#     print(rd.read())

# no need to close the file externally.

# with open("python1.jpg", "ab+") as rd:
#     data=rd.read()
#
# obj = open("python1.jpg", "rb")
# data = obj.read()
# obj1 = open("python2.jpg", "wb")
# obj1.write(data)


# tell(): by using tell I can get the current curser position
# seek(): by using seek we can set the curser position
"""
with open("demo3.txt", "w") as wd:
    wd.write("hello\n")
    print(wd.tell())
    wd.seek(1)
    print(wd.tell())
    wd.write("FIRST")
"""

with open("demo1.txt", "r") as rd:
    # rd.seek(7)
    data = rd.readlines()
    print(data[3])

# print(rd.closed)
#
# obj = open("demo.txt")
# print(obj.closed)

