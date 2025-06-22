# by using comprehesion we can create a other list based conditions and loops,
# it will be a single line expression

# list comprehension:
# find the even numbers from the list
l = [1, 2, 3, 4, 5, 6]
# l1 = [2, 4, 6]
# l1=[]
# for i in l:
#     if i%2==0:
#         l1.append(i)
# print(l1)
# l1 = [i for i in l if i%2==0]
# print(l1)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# divisible 3 and 2
l1= []
for i in l:
    if i%2==0 and i%3==0:
        l1.append(i)
print(l1)

l1 = [i for i in l if i%2==0 and i%3==0]
print(l1)


# dict comprehension:

# d = {k:v for _ in seq}
a = "hello world"

d = {"h":1, "e":1, "l": 3}

d1 = {}

for i in a: #i=h,e, l,l
    if i not in d1: #h,e, l
        d1[i]=1 #d1={"h":1, "e":1, "l:2}
    else:
        d1[i]=d1[i]+1 #d1["l"]=2
print(d1)

d1 = {k:a.count(k) for k in a if k not in ["a","e","i","o","u"]}
d1 = {k:a.count(k) for k in a if a.count(k)==1}
print(d1)

