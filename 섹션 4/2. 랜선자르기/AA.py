# binary search는 <결정 알고리즘> 풀이에 주로 쓰임

# <결정 알고리즘>: 답이 특정 범위에 있음.  a 와 b 사이에 답은 존재한다.


# K개의 각기 다른 길이의 전선을 활용해서
# 같은 길이의 N개의 전선을 만들 것
# 각 전선의 cm는?
# 단 길이는 cm단위로

# 적어도 K개들 중 가장 큰 것보단 안 크겠지. 900, 743, 457, 539
# 그래서 1 ~ 900로 bin search
# 11개 만들어봐
# mid: 500. 그럼 되냐?
# 500으론 총 3개밖에 안 나옴

# 500보다 긴 건 더 안될테니 rt는 499으로

# 1~ 499
# mid: 250    ->  3, 2, 1, 2   8개네..

# 1~ 249
# mid: 125 -> 18개 너무 많음ㅎㅎ  일단 이게 임시 답 res

# 근데 우리 11개 정도 찾고 싶으니까
# 126~249
# mid: 187

import sys

sys.stdin = open('input.txt', 'r')


def count(len):
    cnt = 0
    for x in Line:
        cnt += (x // len)

    return cnt


k, n = map(int, input().split())
Line = []
res = 0
largest = 0

for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest

while lt <= rt:
    mid = (lt + rt) // 2

    if count(mid) >= n:
        res = mid
        lt = mid + 1  #더 좋은 답으로 좁혀가자

    else:
        rt = mid - 1

print(res)