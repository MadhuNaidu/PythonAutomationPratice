"""
Conditional statements: if, elif, else
"""
"""
if condition:
    block code
else:
    code
"""
# Checking multiple conditions
"""
if condition:
    if condition:
        code
    elif condition:
        code
    else:
        code
elif condition:
    code
elif condition:
    code

else:
    code

"""
"""
age = 17
if age>=18:
    print("Candidate is eligible for vote")
else:
    print("Candidate is not eligible for vote due to below 18 age")

if 'amazon_prime'==True:
    print("Able to watch the videos / movies")

elif 'netfilx'==True:
    print("Able to watch netflix movies")

elif 'aha'==True:
    print("Able to watch aha movies")
else:
    print("Please do subscribe")


# Short hand

if age>18:print("eligible for vote")

print("eligible for vote") if age >18 else print('Not eligible for vote')

print("Eligible for vote") if age>18 else print("eligible for vote postal ballet") \
    if age>60 else print("not eligible for vote")
"""
# Loops: by using loops we can perform any repeative task
# for:
# for var in seq:
#     print(var)
# while

l = [1, 2, 3, 4, 5]
s = "hello world welcome to python"
vowels = "aeiou"
l1 = []

# for i in l:
#     print(i)

# for i in s:
#     if i not in vowels:
#         # print(i)
#         l1.append(i)
#
# print("".join(l1))

# range: it will provide range object and we can get all the values
#
# for i in range(10):  # 0-9
#     print(i)
"""
for i in l: #1,
    for j in range(i, len(l)): #1,2,3,4 # 2,3,4,
        print(j)
"""
# while: we don't know how many times it will execute loop,
# first we can check the condition, until condition is false while is going to execute

# while condition:
#     pass
"""
c=0
while c<5:
    print(c)
    c+=1 # c=1,2,3,4,5
"""

# while True:
#     print("hi")

# break: whenever condition satisfied we can use break statement , it will terminate the loop
# once break is executed it won't execute any piece of code
# continue: once continue is executed it will skip the current iteration and
# it won't execute current iteration code after continue
# pass: it won't impact anything but
# it will be used when we want to avoid systax errors to define empty classes, functions etc
games = ["cricket", "volly", "football", "caroms", "chess", "basket ball"]


"""
for i in games:
    if i == "football":
        print(i)
        break
        print("afer break:", i)
    print("outside if condition:", i)

for i in games:
    if i == "football":
        print(i)
        continue
        print("afer continue:", i)
    print("outside if condition:", i)


c=0
while c<5:
    if c==2:
        break
    print(c)
    c+=1

c=0
while c<5: # T, T, T
    c+=1
    if c==2: # c=0,1, 2 F,F, T
        continue
    print(c) # 0,1

for i in l:
    pass


def fun():
    pass
"""

line= "I am living in Bangalore"
# line= "I ma gnivil ni erolagnaB"
words = line.split(" ")
tmp=""
for i in words:
    tmp=i[::-1]+" "+tmp
print(tmp)

# tmp=""
# for i in line:
#     tmp=i+tmp
# print(tmp)

"""
1. what are the condtional statements we have with examples?
2. for and while loops with examples?
3. find the even numbers from the list? add all the even numbers into a list?
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
4. find out duplicate values from the list and print occurences of duplicate values?
# 1 is 2 times
l = [1,3,2,12,21,2,2,1,5,3]
5. find out all the sq of values?
6. find out duplicate values from the string and print occurences of duplicate values? 
7. get the string without vowels / con ?
8. reverse a string? multiple ways?
9. reverse a list?
10. reverse only words from the string statement?
 
"""


"""
# l=[1,2,3,4,5]
# for i in l[::-1]:
#   print(i)
# l1=[i for i in l[::-1]]
# print(l[2::2])

string="Hello welcome to python"
l=[i for i in string.split(" ")[::-1]]
print(" ".join(l))

"""

"""
Write a code snippet to print the following output:
	* * * * *
 	  * * * *
 	    * * *
  	      * *
  	        *
  	       """

"""
def fun(n):
    i = n
    rows = n
    while i >= 1:
        j = rows
        while j > i:
            print(" ", end=' ')
            j -= 1
        k = 1
        while k <= i:
            print("*", end=" ")
            k += 1
        print()
        i -= 1


fun(5)
"""

"""
line= "I am living in Bangalore"
tmp=""
for i in line:
    tmp=i+tmp
print(tmp)
# num = 93281654
# s=0
# for i in str(num):
#     s+=int(i)
# print(s)

"""
