# n = [1, 2, 3, 5]
#
# m = [3, 7]

import sys
import time

start_time = time.time()

# i = input()
# n = list(map(int, input().split()))
# j = input()
# m = list(map(int, input().split()))

n= [1, 10, 27, 39, 50, 61, 65, 70, 93, 93]
m = [7, 51, 65, 66, 70, 82, 93]

i = j = 0
res = []


while i < len(n) and j < len(m):
    if n[i] <= m[j]:
        res.append(n[i])
        i += 1

    else:
        res.append(m[j])
        j += 1

if i < len(n):
    res = res + n[i:]
if j < len(m):
    res = res + m[j:]


#pop보다 위가 빠르네
# res = []
# for i in range(len(n)):
#     for j in range(len(m)):
#         while i < len(n) and j < len(m):
#             if n[i] < m[j]:
#                 k = n.pop(0)
#             else:
#                 k = m.pop(0)
#             res.append(k)
#
# if n:
#     res += n
# else:
#     res += m
#
# for x in res:
#     print(x)

end_time = time.time()

print(end_time - start_time)