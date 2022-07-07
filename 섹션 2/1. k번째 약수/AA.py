# 정수 N의 K번쨰 약수

import sys
# sys.stdin = open("input.txt", "rt")

n, k = list(map(int, input().split()))

cnt = 0

for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)   #return은 함수에서만 사용 가능
        break

else:              #break 없이 와버렸다.
    print(-1)