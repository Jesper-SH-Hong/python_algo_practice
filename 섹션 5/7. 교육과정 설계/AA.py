# 필수과목은 이 순서대로 들어야 함! 또한 반드시 들어야 함.


from collections import deque

req = "CBA"
plan = ["CBDAGE", "FGCDAB"]

dq = deque(req)
print(dq)

# dq.append("CBA")
# print(dq)

for i in range(len(plan)):
    dq = deque(req)  # 필수과목 넣기
    for x in plan[i]:
        if x in dq:
            if x != dq.popleft():
                print("No")
                break
    else:
        if len(dq) == 0:  # ㅇㅋ 순서는 좋았고. 필수는 다 들었나
            print("Yes")
        else:
            print("No")

# res = ""
# l = list(req)
# for x in b:
#     if x in l:
#         res += x
#
# if res == req:
#     print('yes')
# else:
#     print("NO")
