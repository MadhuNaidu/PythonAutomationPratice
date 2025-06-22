# lambda, map, zip, reduce and filter

# it is anounsys function, we can create in a single line.
# lambda function can take args and it will evaluate the expression
# this lambda function we can use in any other special functions
# lambda args: exp
a = 10
# print(a*a)
# lambda_obj = lambda x:x*x
# lambda_obj = lambda x,y: x*y
#
# print(lambda_obj(10, 20))

# map: it will map the values for any function, generally map function can take fun as arg and any sequence as other arg
# map object, we can convert into any seq list, tuple
# map(fun, seq)

#
# def fun(x):
#     print(x*x)
#     return x*x
#
#
# fun(x=10)
# fun(10)
#
# l_obj = lambda x:x*x
#
#
# a = [1, 2, 3, 4]
#
# for i in a:
#     fun(i)
#
# l1 = map(l_obj, a)
# print(type(l1))
# print(l1)
# print(list(l1))


a = [1, 2, 3, 4, 5]


def fun(i):
    # print(i*i)
    return i*i


l_obj = lambda i:i*i

m_obj = list(map(fun, a)) # it will return map obj,  1, 4, 9, 16, 25
l_obj = list(map(l_obj, a)) # it will return map obj,  1, 4, 9, 16, 25
print(m_obj)
print(l_obj)

# fun(a[0]) # 1
# fun(a[1]) # 4



# zip: we can zip the values based on the index positions, it will also return zip object, contains tuple values
# zip(se1,seq2)
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [7, 8]
# # (1,4, 7),(2,5, 8)
# z_obj = list(zip(l1, l2, l3))
# print(z_obj)
#
# a = [1, 2, 3, 4, 5, 6, 7, 8]
#
# total = sum(a)
# print(total)
#
# total = 0
# for i in a:
#     total+=i
# print(total)
#
# total = 0
# n = len(a)
# c = 0
# while c<n:
#     total+=a[c]
#     c+=1
#
# print(total)

# reduce: function as argument and any seq as another args.
from functools import reduce
# reduce(fun, seq)

a = [1, 2, 3, 4, 5]


def fun(i, j):
    return i+j # 3


# sum_of_vals = reduce(fun, a) #i=1,3,6,10,15  j=2,3,4,5
sum_of_vals = reduce(lambda i, j: i+j, a) #i=1,3,6,10,15  j=2,3,4,5
print(sum_of_vals)

# filter: it will take fun as arg and any seq is another agument, here filter can filter the values
# based on the condtion.

a = [1, 2, 3, 4, 5, 6, 7, 8]


def is_even(i):
    return i%2==0

# filter(fun, seq)


f_obj = filter(is_even, a)
f_obj = filter(lambda i:i%2==0, a)
print(list(f_obj))
