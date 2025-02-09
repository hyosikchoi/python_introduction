# add set
thisset = {"apple" , "banana", "cherry"}
thisset.add("orange")
print(thisset)

tropical = {"pineapple" , "mango" , "papaya"}

thisset.update(tropical)
print(thisset)


# remove set
thisset.remove("apple") # 주의할 점 : remove 는 아이템이 존재하지 않을 경우 에러가 난다.

thisset.discard("banana") # discard 는 아이템이 존재하지 않아도 에러가 발생하지 않는다.
print(thisset)


# set 끼리 합치기
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) # set과 다른 타입도 union 으로 합칠 수 있다.
print(set3)

set4 = set1 | set2 # 주의할 점 : | 는 오로지 같은 set 만 join 가능하다!
print(set4)

set5 = set1.union(set2, set3, set4)
print(set5)

myset = set1 | set2 | set3 | set4 | set5
print(myset)

# 교집합 (intersection)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2) # & 로도 가능 but & 도 set 끼리만 가능
print(set3)

# 차집합 (difference)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2) # - 로도 가능 but - 도 set 끼리만 가능

print(set3)