import random as r

# 생성
a = []
c = list()
print(a, c)

a = [1, 2, 3, 4, 5]
print(a)
print(a[0])

b = list(range(1, 11))
print(b)

# 리스트 합치기
d = a + b
print(d)
print()

# 추가하기
a.append(6)  # 뒤에 붙임
print(a)
a.insert(3, 7)  # [3] 인덱스 자리에 7을 넣음
print(a)

# 제거하기
# pop vs remove  위치 vs 해당 값
print(a.pop())  # pop하면 리스트의 맨 뒤에서 빠짐, 리턴 가능함.
a.pop(3)  # [3] 자리의 elem 사라짐
print(a)

a.remove(4)  # 그 값을 제거
print(a)

# 찾는 elem의 인덱스 리턴
print(a.index(5))

# sum, max, min
a = list(range(1, 11))
print(a)
print(sum(a))
print(max(a))  # 최대인 원소 뱉음
print(min(7, 5))  # 7과 5중 최소값

# random
r.shuffle(a)
print("shuffled: ")
print(a)

# sort
a.sort()
print(a)
a.sort(reverse=True)  # 내림차순 소트
print(a)
reversed(a)

a.clear()
print(a)
