"""
class:is a blueprint of objects by using class keyword, it contains attributes, methods etc
object: we can create object for the class, it will represent state, behaviour
self: it represents class reference object
__init__(): constructor, while creating object of the class constructor will be executed.
if we want to initialize any value we use constructor
inheritance: aqeuiring properties from one class another class
single: single child get the properties from single parent
multiple: child can get aquire properties from more than one parent
multilevel:child aquire propertis from parent and another get the properties from child
super(): we can use to call the parent class methods , constructors  etc..
MRO: method resolution order will be helpful to find the order of execution, it will work from left to right
hirachical:
polymorphism:
encapsulation:
abstraction:

code reusability,
"""


class Bank: # class defination
    name = "sbi" # attribute / variable

    def __init__(self, branch): # constructor, instance attributes
        self.branch = branch
        print("const is executed")
        print(f"branch location: {self.branch}")

    def create_account(self): # method, instance method
        print("create user bank account")


class Customer(Bank):
    def __init__(self, customer_name, branch):
        self.customer_name = customer_name
        super().__init__(branch)

    def customer_details(self):
        print("customer details")
        super().create_account()


class Loans(Bank):
    def get_offers(self):
        print("offers from loans")

    def create_account(self):
        print("create account from loans class")


class Insurence(Loans):
    def get_best_offers(self):
        print("best offers")


# obj = Bank("msn", "bangalore") # creating object of the class
# print(obj.name)
# obj.create_account()
obj = Insurence("msn")
obj.create_account()
print(Insurence.mro())
# obj.customer_details()
# obj.create_account()
# print(obj.branch)
# print(obj.username)
class A:
    def greet(self):
        pass


class B(A):
    def greet(self):
        print("greet from b")


class C(A):
    def greet(self):
        print("greet from c")



