a = ["apple", "banana" , "cherry"]
print(a[0]) # apple

print(a[-1]) # cherry


# Change Range items
a[0:2] = ["orange", "watermelon"]

print(a)


# 특정 index 에 insert
a.insert(3,"peach")
print(a)

# Loop of list
for x in a:
    print(x)

# while
x = 0
while x < len(a):
    print(a[x])
    x += 1 

# list comprehension (shortest syntax for looping)
[print(y) for y in a]


fruits = ["apple" , "banana", "cherry", "kiwi" , "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# sort

def myfunc(n):
    return abs(n -50)


thislist = [100,50,65,82,23]

thislist.sort(key= myfunc) # key 에 따른 오름차순 정렬
print(thislist) # [50 ,65 ,23 ,82 ,100]


# copy

copylist = thislist.copy()
copylist2 = thislist[:]
print(copylist)
print(copylist2)


# join
list1 = ["a" ,"b" , "c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

