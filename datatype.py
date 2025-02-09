# str
x = "Hello world"

# int
x = 20

# float
x = 20.5

# complex
x = 1j

# list
x = ["a" , "b" , "c"]

# tuple (immutable 한 순서가 있는 collection)
x = ("a" , "b" , "c")

# range (연속된 숫자 범위를 생성하는 객체, 주로 for문에서 사용, 리스트와 비슷하지만 메모리를 적게 사용)
x = range(6)
print(list(x))
print(x[1])

for i in x:
    print(i, end=" ")

# dict
x = {"name" : "John", "age" : 36}

# set
x = {"apple" , "banana" , "orange"}

# frozenset (immutable 한 set 으로 dict 의 key 로 사용가능)
x = frozenset({"apple", "banana", "cherry"})

# bool
x = True

# bytes
x = b"Hello"
print(x)

# bytearray
x = bytearray(5)
print(x)

# memoryview
x = memoryview(bytes(5))

# NoneType
x = None