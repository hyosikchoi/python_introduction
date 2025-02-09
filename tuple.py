# 튜플은 중복은 허용하지만 한 번 생성하면 수정,추가,삭제 불가
mytuple = ("apple" , "banana" , "cherry", "apple")

# 튜플은 속성을 한개로 하면 튜플로 인식 안한다. 대신 , 를 포함하면 가능하다
isTuple = ("a")
isTuple2 = ("a",)
print(type(isTuple)) # str
print(type(isTuple2)) # tuple


# 추가 하기 위한 방법
# 튜플 + 튜플로 추가할 수 있다. 
thistuple = ("apple" , "banana" , "cherry")
y = ("orange",)

thistuple += y
print(thistuple)


# 구조 분해시 kotlin vararg 처럼 사용 하기 위해 *(asterisk) 사용가능
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green) # apple
print(tropic) # [mango, papaya, pineapple]
print(red) # cherry


# 튜플 곱하기
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)