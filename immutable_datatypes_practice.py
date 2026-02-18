"""
name = "Madhu sudhana naidu" # 0,1,2
print(type(name))
print(dir(name))

# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
print(name.capitalize()) # Madhu naidu
print(name.count('a'))
print(name.count('dh'))
print(name.find('m'))
print(name.index('a'))
names = ("madhu", "sudhana", "naidu")

print(" ".join(names))
a = " hey are you listing python class "
print(a.strip(" "))
print(a.lstrip(" "))
print(a.rstrip(" "))
print(name.title())
print(name.swapcase())
print(name.split(" ")) # it will return list of words
# print(a.replace('Hey', 'Hi'))
print(a.isdigit())
print(a.isupper())
print(a.islower())
print(a.istitle())
"""
# tuple:
# a = (1, 2, 3, 4, "madhu", 2, 1, 4) # 0, 1, 2, 3, 4
# print(type(a))
# print(dir(a))
# print(a.count(4)) # 2
# print(a.index(2)) # 1
# print(id(a))

a = 10
b = 10


print(id(a))
print(id(b))

a = 13
print("after value update:", id(a))

l= [1, 2, 3]
l1= [1, 2, 3]

print(id(l))
print(id(l1))