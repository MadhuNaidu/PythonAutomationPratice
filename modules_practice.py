# module: is a kind of python file
# os, datetime, re, json, functools
import os

print(dir(os))
# print(os.getcwd())
# print(os.listdir())
# print(os.path.isfile("first_program.py"))
# os.mkdir("os_module_practice")
# print(os.path.isdir("os_module_practice"))
# os.chdir("os_module_practice")
"""
print(os.getcwd())
with open("os_module_practice_1.txt", "w") as wr:
    wr.write("I am learning os module")
# os.system("cd ..")
print(os.getcwd())
# print(os.path.join())
print(os.getenv("path"))
# how to find the only text files from the folder and it's subfolders?
for dir, subdir, file in os.walk("C:\\Users\madhusudhana_naidu\PycharmProjects\python_practice\Python_practice_may_2025"):
    # print("DIR:", dir)
    # print("Sub DIr:", subdir)
    for f in file:
        if f.endswith(".txt"):
            print("File:", f)
"""
# How we can create nested dir
# os.mkdir("demo4")
# if not os.path.isdir("demo1/demo2/demo3"):
#     os.makedirs("demo1/demo2/demo3")
# os.rmdir("demo4")
# os.rmdir("demo1/demo2/demo3")
# os.remove("demo.txt")
# os.rename("demo.txt", "demo1.txt")

# print(os.system("dir"))
# data=os.popen("dir")
# print(data.read())

print(os.getenv("path"))
print(os.getenv("TEMP"))
print(os.environ)
# os.putenv()