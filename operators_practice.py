"""
What is a operator:
it is a symbol that can perform certain action.
Arithmetic operators: we can perform arithmetic operations, +,-,*,/,//,%, **
Assignment operators: =, +=, -=, *=,/=, //=, %=, **=
Comparison operators: ==, <, >, <=, >=, != ( Boolean value)
Logical operators: and, or, not ( Boolean values ) , we can evaluate expression
Identity operators: is, not, we can compare the objects not the values, it will return boolean value
Membership operators: in, not in, we can use to check the values, it will return boolean
Bitwise operators: &, |, ^, ~ >>, <<
"""
a = 10
b = 20
# c = "Hello"
# d = "Python"
# print(a+b)
# print(c+d)
# print(a-b)
# print(a*b)
# print(a/b) # 10/20
# print(a//b)
# print(5%2)
# print(2**2)

# a+=10
# # a = a+10
#
# print(a) # 20
# a-=5
# print(a) # 15
# a*=3
# print(a) # 45
# a/=5
# print(a) # 45/5 = 9.0
# a//=3 # 9.0//3, 10//3
# print(a) # 3
# a**=2
# print(a)

a = 10
b = 20
c = 30
# print(a==b)
# print(a<b)
# print(a>b)
# print(a!=b)
# print(10<10)
# print(10<=10)
# print(10>=10)

# and
# True    True    True
# True    False   False
# False   True    False
# False   False   False

# or
# True    True    True
# True    False   True
# False   True    True
# False   False   False

# not
# True    False
# False   True

# a = 10
# b = 20
# c = 30
# print(a>b and a>c) # False
# print(a<b and a<c) # True
# print((a<b and a<c) and (b<c)) # True
# print((a<b or a>c) and (b<c)) # True
# print((a>b or a>c) or (b>c)) # False
# print(not(a>b or a>c) or (b>c)) # True
#

# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a
#
# print(id(a))
# print(id(b))
# print(id(c))
#
# print(a is b)  # False
# print(a is c)  # True
# print(a is not c)  # False
#
# l1 = [1, 2, 3, 4]
# print(3 in l1)
# print(33 in l1)
# print(3 not in l1)
# print(33 not in l1)

"""
0000 - 0
0001 - 1
0010 - 2
0011 -3
0100 - 4
0101 - 5
"""
a = 1
b = 2

print(a&b)
