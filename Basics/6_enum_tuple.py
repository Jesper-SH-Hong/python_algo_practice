


a = [15, 20, 25]
for i in range(len(a)):
    print(a[i], end=' ')
print()

# for x in a:
#     print(x, end=' ')
# print()

for x in enumerate(a):  # (인덱스, 값) 리턴
    print(x)

for x in enumerate(a):
    print(x[0], x[1])

print("i, val로도 가능")
for index, val in enumerate(a):
    print(index, val)


b = [1, 2, 3, 4, 5]
b[0] = 2
print(b)

#tuple
b = (1, 2, 3, 4, 5)
# b[0] = 2   - 에러: immutablㄷ


if all(60 > x for x in a):
    print("Yes.. smaller than 60")
else:
    print("No")

#any 하나라도 참이면 만족
if any(19>x for x in a):
    print("yes, one of them < 19")
else:
    print("Nothing..")