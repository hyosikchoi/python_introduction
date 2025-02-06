# Multiline Strings

a = """
    Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
"""

b = "Hello"

print(a)
print(b[1]) # e


# Looping a String
for x in "banana":
    print(x, end="")

print(len(b))


# Check txt

c = "ipsum" in a
print(c)

d = "aaa" not in a
print(d)


# Slice
x = "Hello , World!"
print(x[:5]) # 5미만 
print(x[5:10]) # 5이상 10미만

print(x[-5:-1]) # 인덱스를 역순으로 orld 출력


# trip
x = " aa "
print(x.strip())


# Format String
age = 36
txt = f"My name is hyo, I am  {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars" # 소수점 2째자리 까지 보여줌
print(txt)


def myFunc() :
    return True

print(myFunc())