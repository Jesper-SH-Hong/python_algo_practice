# 문제 이상. 비교 대상이 전체가 아니라 이미 훑은 지원자인 것임. 갱신형... ㅋㅋㅋ


import sys

sys.stdin = open("input.txt", 'r')
n = int(input())

body = []

for i in range(n):
    a, b = map(int, input().split())
    body.append((a, b))

body.sort(reverse=True)  # 첫 아이템에 대해 내림차순 정렬

largest = 0
cnt = 0  # 선발인원

for x, y in body:
    if y > largest:
        largest = y
        cnt += 1

print(cnt)
