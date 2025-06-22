# generally type casting means converting one data type to other data type.
a = 10
b = "Hello11"
b1 = "11"
c = (1, 2, 3)
d = [1, 2, 3]
e = {"a": 1, "b": 2, "c": 3}
f = {1, 2, 3}

# int(), str(), tuple(), list(), dict(), set()

print(int(b1)) # type casting
# print(int(b)) # type casting

print(str(a))
print(str(c)[2])

# print(tuple(a))
print(tuple(b))
print(tuple(d))
print(tuple(e))
print(tuple(f))

a = ""
b = tuple()
b1 = (1,)
b2 = (1)
print(type(b1))
print(type(b2))
c = [1]
d={}
s=set()
