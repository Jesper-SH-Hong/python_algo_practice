# 최대힙: 루트가 최대값

# heapq는 기본적으로 최소힙 방식으로 가동함..
# heappush 시 무조건 최소힙으로 만듬
# heappop(a)을 해도 최소힙으로 작동함.
# 그래서 그냥 부호를 바꿔서 넣어버림.  3, 4가 아니라 -3, -4로.

#  3     ->   -4
# 4         -3


import sys
import heapq as hq

sys.stdin = open('input.txt', 'r')


a = []
while True:
    n = int(input())
    if n == -1:
        break

    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))  #다시 원 부호로
    else:
        hq.heappush(a, -n)  # 부호 바꾸기
