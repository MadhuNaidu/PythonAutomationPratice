
# this code is written to understand comments in python
"""
This is for understanding multiline comments in python
"""
# print("hello world")out comments in python")

# Variables: we can store the values in form any type, by using = assigment operator we can assign the values

# string datatype
name = "Madhu"
phone = '7799884799'
emp_id = 1

t = (1, 2, 4, "madhu")

l = [1, 2, 3, 'madhu']
s = {1, 2, "madhu"}
d = {'a': 1, "b": 2}

# print(name)
# print(phone)
"""
datatypes:
int, str, tuple: immutable datatypes, Once we define we cannot change throught life span
list, dict, set: mutable datatypes, we can able to add, update and delete the items
"""

"""
inbuilt methods: 
type(): it will return what type of object it is.
"""
# print(type(name))
# print(type(123))
# print(type((1, 2, 3)))
# print(type([1, 2, 3]))
# print(type({1, 2, 3}))
# print(type({1: 1, 2: 2, 3: 3}))

# id: this method will return memory location of a variable
# print(id(name))
# print(id(t))
# print(id(l))

# dir: it will display the available methods to the object.
# print(dir(name))
# help, min, max, sum(), len()

# magic methods or dunder methods
# print(dir(int))

"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 
'index', 'isalnum', 'isalpha',
 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
  'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower'
, 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
"""

s = "msn python automation testing"
# print(s.islower())
# print(s.isupper())
# print("Hello".isupper())
# print("123".isdigit())
# print("123hel".isdigit())
# print("123hel".isalnum())
# print(s.title())
# print(s.capitalize())
# print(s.find('th'))
# print(s.replace('python', 'playwright'))
# print(s.split(" ")) # list of words
# print(" ".join(s.split(" ")))
# print(s.count('m')) # 2
# print(s.count('ti')) # 2
# print(s.count('msn')) # 1
# print(s.count(' ')) # 3
#
# print(s.index('n')) # 2
# name = "madhu"
# print(id(name))
# # print(name.title())
# print(name)
#
# name.title() # madhu
# print(id(name))
# print(name)

# l = [1, 2, 3]
# print(id(l))
# print(l)
# # print(dir(l))
# l.append(4)
# print(id(l))
# print(l)
#
# l.append(5)
# print(id(l))
# print(l)

# t = (1, 2, 1, "hello")
# print(dir(t))
# print(t.count(1)) # 2
# print(t.index(2)) # 1
# print(t.index(1)) # 1
# print(t.index(10)) # Value Error

l = [1, 2, 3, "hello"]
# # append: it will append the single value at end of the list
# l.append(4)
# print(l) # [1, 2, 3, "hello", 4]
# # insert: it will take 2 args, index, value
# l.insert(2, 100)
# print(l) # [1, 2, 100, 3, "hello", 4]
# # extend: we can use to extend the list with list of values, it will add the values at the end
# l.extend([10, 20, 30])
# print(l) # [1, 2, 100, 3, "hello", 4, 10, 20, 30]
# l1 = [40, 50]
# l.extend(l1)
# print(l) # [1, 2, 100, 3, "hello", 4, 10, 20, 30, 40, 50]
# pop: it will remove the last item from the list and it will return the value
# print(l.pop())
# print(l) # [1, 2, 3]
# # remove: it will remove only the particular value
# print(l.remove(2))
# print(l)
# l.clear() # it will clear all the items in a list, list will become a empty
# print(l)
# l = [1, 2, 5, 6, 3, 58, 23]
# l.sort() # it will be useful to sort the list, by default ascending order
# print(l)
# l.sort(reverse=True)
# print(l)
# l.reverse()
# print(l)

# nested list means list inside list
# l1 = [1, 2, [3, 4], 5, [6, 7, [8, 9]]]
# # print(len(l1))
# print(l1[0]) # slicing
# print(l1[2]) # slicing
# print(l1[2][0])
# s = "hello"
# print(s[0])
# print(s[1])
# sequence / hashable data types: str, tuple, list
"""
 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

"""
dict: it is a mutable datatype, we can use data mapping, data will be mapped as a key value pair
d = {"key1": "value1", "key2": "value2"}
key should be only immutable datatype, int, str, tuple. key should be unique
value can be anything and it will allow duplicates as well
"""
# candidate_details1 = {"name": "msn", "place": "bng", "id": 1}
# candidate_details2 = {"name": "msn", "place": "bng", "id": 1, "name": "MSN"}
# candidate_details3 = {("name", "place"): ["msn", "bng"], "place": "bng", "id": 1}
# print(candidate_details1)
# print(candidate_details2)
# print(len(candidate_details1))
# print(len(candidate_details2))
# print(candidate_details3)

user_details = {"name": "msn", "address": {"place": "bng", "pin": 534563, "dno": 234},
                "courses": ["python", "playwright", "selenium"]}

# print(user_details["address"]["pin"])
# print(user_details["courses"][1])
# user_details["courses"][2] = "api"
# print(user_details)
# keys=name, address
# print(dir(user_details))
# print(user_details.keys())
# print(user_details.values())
# print(user_details.get('name')) # msn, if key is not there in dict it will return None
# print(user_details.get('name1'))
# user_details.update({"course": "playwright", "duration": 60})
# print(user_details)
# user_details['domain'] = "QA" # added new key value pair
# user_details['course'] = "Python"
# print(user_details)
# print(user_details['course']) # it will return value corresponding key
# print(user_details['course1']) # if key is not there in dict, it will through KeyError
# print(user_details.pop("name")) # it will take key as a arg and it will pop the key value and return value
# print(user_details.popitem()) # it will pop the last item from dict and it will return key value pair as a tuple
# items: it will return tuple of key value pairs
# print(user_details)
# print(user_details.items()) # it will return list of tuples
# ("name", "msn"), ("address", {""})
"""
'keys': it will return the keys from the dict
'values': it will return the values from the dict
'clear', 'copy', 'fromkeys', 'get', 'items', 'pop', 'popitem', 'setdefault', 'update', 'values'
"""

"""
set: it is a mutable datatype, we can define by using { }, set won't allow duplicate values

"""

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6, 5, 4}
s3 = {4, 5, 6}

print(dir(s1))

print(s1.union(s2)) # {1, 2, 3, 4, 5, 6}
print(s1.intersection(s2)) #{3, 4}
print(s3.issubset(s2)) # True
print(s2.issuperset(s3)) # True
"""
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'
"""
