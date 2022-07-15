import sys
# sys.stdin = open("input.txt")

n, m = map(int, input().split())

a = list(map(int, input().split()))

# a = [1, 2, 1, 3, 1, 1, 1, 2]
# n = len(a)
# m = 3

# acc = 0
# cnt = 0
#
# for i in range(len(a)):
#     acc += a[i]
#     for j in range(i, len(a)):
#         if acc + a[j] == m:
#             cnt += 1
#             acc = 0

lt = 0  # left  # right
rt = 1
tot = a[0]  # lt ~ rt 하나 앞
cnt = 0

# while True:
#     if tot < m:
#         if rt < n:
#             tot += a[rt]
#             rt += 1
#         else:
#             break
#     elif tot == m:
#         cnt += 1
#         lt += 1
#         tot = 0
#     elif tot > m:
#         tot += a[rt]
#         rt += 1
#         lt += 1

sum = a[0]

while True:
    if sum < m:
        if rt < n: ####   index인 rt가 n인 경우.. 또 rt를 다음칸으로 +1 말고 탈출하자.
            sum += a[rt]
            rt += 1
        else:
            break
    elif sum == m:
        cnt += 1
        sum -= a[lt]
        lt += 1
    else:
    # if lt == rt:     신경 X. lt가 rt까지 왔으면 sum =0 일테니 다시 rt +=1로 감. 그러다 rt < n 조건에서 멈출 것. sum < m이 유일한 rt 밀어내기 조건..
    #     rt += 1
    #     sum = a[lt]

        sum -= a[lt]
        lt += 1

print(cnt)
