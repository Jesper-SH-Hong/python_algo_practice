# Queue 자료 구조. FIFO. 입출구가 다름. 세차장

# 파이썬의 queue는 deque라는 자료구조임.

# deque는 앞에서도 넣거나 꺼낼 수 있음. appendleft, popleft.
# 뒤에서 넣을떈 append, pop


# K번째 왕자가 빠지고, 다시 그 다음 왕자가 1번이 되어 또 K번쨰 놈을 뺴는 거임
from collections import deque

n = 8
k = 3

a = list(range(1, n+1))
dq = deque(a)

while len(dq) > 1:
    for _ in range(k-1):
        dq.append(dq.popleft())
    dq.popleft()

print(dq[0])


#선생 풀이:
# while dq:
#     for _ in range(k-1):
#         cur = dq.popleft()
#         dq.append(cur)
#     dq.popleft()
#     if len(dq) == 1:
#         print(dq[0])
#         dq.popleft()
