# list , dict , set

l = [1, 2, 3, 4, 'Madhu', 23.23]
l = [1, 2, 3, 4, 'Madhu', 23.23, [35, 45, 50, 65, 43, 55]]
# print(l[6][2])

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
#
# print(type(l))
# print(dir(l))
# l.append(25) # append it will add the item in end of the list
# # [1, 2, 3, 4, 'Madhu', 23.23, 25]
# print(l)
# l.insert(0, 100) # insert method will insert the value at particular index position,
# # it will take two args index and value
# # [100, 1, 2, 3, 4, 'Madhu', 23.23, 25]
# print(l)
# l.extend([20, 30, 40]) # extend can extend the list with another list or sequences
# # [100, 1, 2, 3, 4, 'Madhu', 23.23, 25, 20, 30, 40]
# print(l)
# l.pop() # it will remove the last item and return the value
# # [100, 1, 2, 3, 4, 'Madhu', 23.23, 25, 20, 30]
# print(l)
# l.pop(1) # 1
# # [100, 2, 3, 4, 'Madhu', 23.23, 25, 20, 30]
# print(l)
# l.remove(4) # it will remove the particular value
# print(l)
# l = [1, 2, 3, 4, 10, 5, 15, 6]
# # l.sort() # it will sort the list and by default asending order
# # print(l)
# # l.sort(reverse=True)
# # print(l)
# # print(l.pop(3))
# l = [1, 2, 3]
# l1 = l.copy() # it will copy all the items from l to l1, deep copy
# # print(id(l))
# # print(id(l1))
# l2 = l # it will copy all the items from the l to l2, shallow copy
# # print(id(l2))
# l.append(10)
# # l=[1, 2, 3, 10]
# print(l)
# print(l2)
# print(l1)
# l2.append(100)
# print(l)
# print(l2)
# print(l1)
# l.clear() # it will remove all the items but empty list will be there.
# print(l)
# print(l2)
# print(l1)


# dict: {key1: value1, key2: value2}
# dict can contain key value pairs and key should be unique, it cannot allow duplicate
# we can use dict for doing data mapping
# We can create nested dict

user_details = {"first_name": "Madhu", "last_name":"Naidu",
                "Company": "Sony", "Role": "QA Eng", 1:"UserID", "first_name":"madhu", ("sal", "dept"):(30000, 'QA'),
                "address":{
                    "Dno":11,
                    "Village":"Marathalli",
                    "Street": "Balaji Layout",
                    "Pincode": 560067,
                    "State": "KA",
                    "Personal_details":
                        {
                            "Blood_group":'A+',
                            "Gender": 'Male',
                            "DOB":'16/06/1993',
                            "Hobbies": ["Singing", "Reels", "Cricket", "Movies", "Chess"]

                        }
                }}

# print(dir(user_details))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# print(user_details.get("first_name")) # if there is no key, it won't return anything
# print(user_details.get("First_name")) # if there is no key, it won't return anything
# print(user_details.keys())
# print(user_details.values())
# print(user_details["first_name"]) # if there is no key it will throw the KeyError
# # print(user_details["First_name"]) # if there is no key it will throw the KeyError
# user_details.update({"phone": 7799884799})
# print(user_details)
# user_details["Place"]="Bangalore"
# print(user_details)
# print(user_details.items())
# print(user_details.popitem()) # it will remove last key and value and return the value

# print(user_details.pop("Role"))

# print(user_details.get("address")["Personal_details"]["Hobbies"])
# print(user_details.get("address")["Personal_details"]["Hobbies"][0])
# user_details["address"]["Personal_details"]["Hobbies"][1]="Boxing"
# print(user_details)


# set:
#
# s1 = {1, 2, 3, 4}
# s2 = {5, 6, 7, 8}
# s3 = {1, 2}
#
# print(type(s1))
# print(id(s1))
# print(dir(s1))


# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
# 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.intersection(s3))
# print(s1.difference(s3))
# print(s1.add(20))
# print(s1)
# s1.update({30, 40, 50})
# print(s1)
# print(s1.pop())
# s1.remove(40)
# print(s1)
# print(s1.pop())

l= [1, 2, 3, 4, 5, 6]


# [start: stop: step]

print(l[3])
print(l[3])
print(l[-1])

print(l[0:4]) # start is included and stop is excluded
print(l[0:]) # start is included and stop is excluded
print(l[1::2]) # start is included and stop is excluded
print(l[-4:-1]) # start is included and stop is excluded

"""
1. What are the python charecterstics?
2. What is a python path?
3. what are the datatypes with examples?
4. What are the inbuilt methods with examples?
5. string methods with methods?
6. list methods with examples?
7. diff b/w list and tuple?
8. diff b/w insert, append and extend?
9. diff b/w pop and remove, clear?
10. diff shallow and deep copy with example?
11. how to sort a list with ascending and descnding order?
12. What is a dict and where to use?
13. how many ways we can get the values from dict?
14. how many ways we can update the dict?
15. diff b/w pop and popitem()?
16. what are the available methods in sets?
17. What is a slicing? examples?
18. What is a index in python and how it will be useful?
19. Find the largest, second largest and lowest, second lowest num for the list?
20. Sort the list?
21. Sort the list without inbuilt functions?



"""
