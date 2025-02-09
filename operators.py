# exponentiation
x = 2
y = 5
print(x**y) # 2 * 2 * 2 * 2 * 2


# 윌러스 연산자 (값을 할당하면서 바로 비교하거나 가능) (파이썬 3.8 이상부터 사용 가능)

# 기존 방식
numbers = [1, 3, 7, 10, 15]
filtered = []
for n in numbers:
    if n > 5:
        filtered.append(n)
print(filtered)  # [7, 10, 15]


# 윌러스 연산자 사용
numbers = [1, 3, 7, 10, 15]
filtered = [n for n in numbers if (x := n) > 5]
print(filtered)  # [7, 10, 15]
