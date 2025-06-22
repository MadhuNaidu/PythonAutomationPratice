# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(a.__sizeof__())
# print(a)

# iter((1, 2, 3, 4))
# for i in a:
#     print(i)
# iterators: it is a function, any sequence we make it a iterator by using iter function.
# iterator can hold only object reference because of that size is less.
# we can utilize memory properly, here iterators are lazy calling.
# Once we get all the values from the iterator it will throw StopIterationException
"""
# b = iter(a)
b = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
# print(type(b))
print(b.__sizeof__())
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
"""
# generators are used to create iterators in
# simple way and we can use yield keyword to return the value instead of return in a function
# we can use next method to call generator object.
# memory will be utilized properly

"""
def sq_numbers(n):
    for i in range(n): # start, stop, step
        yield i*i
    # yield 1
    # yield 2
    
    

obj = sq_numbers(5)
# print(type(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))



def get_numbers(n): # function defination with args
    # function body
    yield n*1
    yield n*2
    yield n*3
    yield n*4
    yield n*5
    yield n*6
    yield n*7
    yield n*8
    yield n*9
    yield n*10


obj = get_numbers(2) # function calling by using function name
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

"""
# decorator: without modifying original functionality / features we can
# provide additional / extra features to the function
# decorator can take funcation as a args and it will return a function
# dec can have inner / wrapper func
# by using @ notation / symbal to call the dec on top off functions


def dec_fun(fun):
    def inner(festive_name):
        # additional features
        print("It's weekend")
        fun(festive_name)
    return inner


def dec_festive(fun):
    def inner(festive_name):
        print("Celebrate {} festival".format(festive_name))
        fun(festive_name)
    return inner


@dec_fun
@dec_festive
def normal_fun(festive_name):
    print("Routine work")


# normal_fun(festive_name="Dasara")
# normal_fun(festive_name="Deepavali")

# sometimes we have to provide fun args


def dec_add(fun):
    def inner(a,b):
        print(a+b)
        fun(a,b)
    return inner


def dec_sub(fun):
    def inner(a,b):
        print(a-b)
        fun(a,b)
    return inner


@dec_add
@dec_sub
def num_fun(a,b):
    pass

num_fun(10,20)