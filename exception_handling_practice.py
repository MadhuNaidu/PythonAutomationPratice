# Exceptions:
# Error: this is made by us, we cannot handle, it will break the execution flow
# Exception: we can handle by using try, except, else, finally blocks

# print("Hello world")


def values_division(a, b):
    try:
        # actual code to perform division
        print("Try block started")
        c = a / b
        # print("Result:", c)
        c = {a: b}
        print(c[100])
        # print(c.get())
    #     sqlite db connection
    # sql querires
    except ZeroDivisionError as e:
        # print("Got the exception in try block, so I am handling here.")
        print("Exception:", e)
        # print(b/a)
        # print("If there is no exception in try block, except block won't execute")
    except KeyError as e:
        print("Got the Keyerror :", e)
    except ValueError as e:
        print("Value Error")
    except FileNotFoundError as e:
        pass
    else:
        print("It is going to execute when there is no exception")
    finally:
        print("it will execute everytime, irrespective of try and except blocks")
        # let's you have db connection in try
#         teardown activities / closing session

# values_division(a=10, b=20)
# values_division(10, 0)
# raise: by using raise we can raise custom exceptions
# NegativeNumError


class NegativeNumError(Exception):
    pass


def fun(a):
    if a<0:
        raise NegativeNumError("Erorr negative")
    else:
        print("No exception")


# fun(10)
# fun(-2)

# First create function
# use exception handling mechanism

# find given num is even or odd


def is_even(n):
    try:
        if n%2==0:
            return "Even"
        else:
            return "Odd"
    except ValueError as e:
        print("Got the exception:", e)
        return "Invalid data"
    except TypeError as e:
        print("Type error:", e)
        return "Invalid data"


print(is_even(9))
