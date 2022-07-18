import sys

# sys.stdin = open("input.txt", "rt")
# n = int(input())


# 1 2 3 4 5 6 7 8
#[0 0 0 0 0 0 0 0]   -ch
# 1은 소수니까 제끼고 2 부터 n까지 iterate
# 0 1 0 1 0 1 0 1
# 0 1 ! 1 0 ! 0 1
# 0 1 ! 1 0 ! 0 1
# 0 1 1 1 ! 1 0 1
# 0 1 1 1 ! 1 1 1

#cnt는 소수인 경우, 즉 아직 0인 경우 체크

n = 20

ch = [0] * (n+1)
cnt = 0

for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(2, n+1):
            if j % i == 0:
                ch[j] = 1

print(cnt)