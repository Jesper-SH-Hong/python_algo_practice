# n = list(range(1, 21))
#
# print(n)
#
#
# def reversing(n, a, b):
#     for i in range(0, (b-a) // 2):
#         tmp = n[a-1+i]
#         n[a-1+i] = n[b-1 - i]
#         n[b-1-i] = tmp
#         print(n)
#
#
# reversing(n, 1, 5)
# print(n)

import sys
sys.stdin = open("input.txt", "r")

a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i]   =   a[e-i], a[s+i]     #swap
        
print(a)
a.pop(0)  #pop은 제일 뒤. 맨 앞자리는 0번 인덱스

for x in a:
    print(a, end=' ')