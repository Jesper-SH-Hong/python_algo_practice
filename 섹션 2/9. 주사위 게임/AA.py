import sys
sys.stdin = open("input.txt", "rt")
n = int(input())

res = 0
for i in range(n):
    tmp = input().split()   #str의 리스트
    #print(tmp)
    tmp.sort()
    a, b, c = map(int,tmp)
    #print(a,b,c)

    if a == b and b == c:       # if,elif문. 위에서 걸리면 더 안 돌고 끝나니 케이스 구분 잘할 것
        money = 10000 + a*1000
    elif a == b or a == c:   #뭐가 됐든 a로 계산하면 되니..
        money = 1000 + (a*100)
    elif b == c:
        money = 1000 + (b*100)
    else:
        money = c * 100

    if money > res:
        res = money

print(res)