import sys
# sys.stdin = open('in2.txt', 'r')
n = int(input())
a = list(map(int, input().split()))

# n = 5
# a = [2, 4, 5, 1, 3]

lt = 0
rt = n - 1
cnt = 0
res = ""
prev = 0  # 이전에 추출한 항보다는 커야 하니까
tmp = []

while lt <= rt:
    if a[lt] > prev:
        tmp.append(  (a[lt], "L")   )
    if a[rt] > prev:
        tmp.append(  (a[rt], "R")   )

    tmp.sort()   #튜플[0] 기준으로 정렬

    if len(tmp) == 0:  # 더 이상 가져올 자료가 없음.
        break

    else:         #두 튜플 중 첫 자료
        res += tmp[0][1]
                     #그 중 알파벳
        prev = tmp[0][0]

        if tmp[0][1] == 'L':
            lt +=1
        else:
            rt -=1
    tmp.clear()

print(len(res))
print(res)


#아래 답은 time limit 발생

# while a[0] > prev or a[-1] > prev:
#     if a[0] < a[-1] and a[0] > prev:
#         prev = a[0]
#         a.pop(0)
#         lt += 1
#         res += "L"
#         cnt += 1
#     elif a[-1] > prev:
#         prev = a[-1]
#         a.pop()
#         rt -= 1
#         res += "R"
#         cnt += 1
#
#
#
# print(cnt)
# print(res)
