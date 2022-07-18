import sys
# sys.stdin = open("input.txt", "rt")


#4면체, 4면체 = 1,2,3,4   vs 1,2,3

#   |1_2_3_4
#   ---------
# 1 |2 3 4 5
# 2 |3 4 5 6
# 3 |4 5 6 7

# cnt array에 각 결과값들의 개수를 세자. 2가 나오면 idx 2에 넣자.


# n, m = map(int(input().split()));

n = 6
m = 4

cnt = [0] * (n+m+1)    # n+m+1인덱스에 n+m이 들어가게 될테니
max_ = -2147000000

for num1 in range(1, n+1):
    for num2 in range(1, m+1):
        cnt[num1 + num2] += 1

for i in range(n+m+1):
    if cnt[i] > max_:
        max_ = cnt[i]

for i in range(n+m+1):
    if cnt[i] == max_:
        print(i, end=' ')

print(cnt)