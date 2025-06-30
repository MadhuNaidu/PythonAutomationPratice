# function is a block of code, that can perform particular task
# inbuilt functions: which can directly call the function without define,
# once we install python automatically we can use it.
# ex: type, dir, help, id, max, min, join, strip, split, sort, count, extend, append, pop, popitem
# user defined functions: user defined functions are defined by us by using def keyword
#function can return the values, in a function return only once it will execute,
# but we can multiple return statements
# type()

# def fun_name():# function defination
    # function body

# fun_name() # function calling
# code reusable
"""
def fun(hero, herione, year=2018): # function defination with args hero, herione
    if year == 2018:
        print("F1 movie")
        print("Hi {} and Hi {}".format(hero, herione))
        return 2018
    elif year == 2019:
        print("F2 movie")
        print("Hi {} and Hi {}".format(hero, herione))
        return 2019
    else:
        print("F3 movie")
        print("Hi {} and Hi {}".format(hero, herione))

"""
# fun("Venky", "Tamanna")
# fun("Tamanna", "Venky")
# fun(herione="Tamanna", hero="Venky", year=2019)
# fun("Tamanna", "Venky", year=2019)

# positional args:
# default args:
# variable length args ( *args ):
# variable length keyword args ( **kawgs ):


# def fun(id, course="python", *args, **kwargs): # args is a list of variables
#     # for i in args:
#     #     print(i)
#     print(id)
#     print(course)
#     print(args)
#     print(kwargs)
#
#
# fun(1, "Python", "f1", "f2", "f3", "f4", name="Madhu", place="Bangalore")
# fun("f1", "Selenium", "f2", "f3", "f4", "f5", "f6", name="MN")
# fun("f1", "API", "f2", "f3", name="MN", place="Bng", Sports=["Chess", "Cricket", "Volly"])


def fun(movie_name, amount):
    print("{} is collected amount {}".format(movie_name, amount))
    return amount


# amount_collected = fun("F1", 180)
# print("Amount is collected after 3rd week:", amount_collected)
# amount_collected = fun("Pushpa1", 380)
# print("Amount is collected after 3rd week:", amount_collected)

a = "Hello world"
a.split(" ")
# special functions


def movie_rating(movie, rating):
    print("{} rated: {}".format(movie, rating))