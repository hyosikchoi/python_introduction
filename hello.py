import sys

print("Hello, World!")
print(sys.version) # 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)]

if 5 > 2:
    print("Five is greater than two!")
    print("Five is greater than two!")

x = 5 # x type int
x = "Sally" # x is now of type str
y = "Hello, World!"

print(x, y)


a = str(3)
b = int(3)
z = float(3)

print(a,b,z) # '3', 3 , 3.0

# Multiple Variables

x, y, z = "Apple", "Banana" , "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# Global variables

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)
