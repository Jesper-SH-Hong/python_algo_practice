# import sys
# import itertools as it
# #sys.stdin=open("input.txt", "r")
# n, k=map(int, input().split())
# a=list(map(int, input().split()))
# m=int(input())
# cnt=0
# for x in it.combinations(a, k):
#     if sum(x)%m==0:
#         cnt+=1
# print(cnt)

# 위는 라이브러리 사용한 답인듯




#5(n)개의 정수 중 3(k)개로 만든 조합의 원소합이 m의 배수인 경우는?
# [2,4,5]
# [2,4,8]
# [2,4,12]
# .....
# [5,8,12]





# 바로 앞 문제에서 봤듯 조합은 DFS()에 for문이 도는 시작 지점 s가 있어야 함!!

def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s,n): #이번엔 n이야 n+1 아님ㅋㅋ 전문제는 원소가 1~n이었고, 지금은 a'리스트'의 원소니 idx 써야
            DFS(L+1, i+1, sum + a[i])   #sum이 leaf 닿으면 옆/전? 가지를 위해 초기화되야할테니 DFS에 낑껴야겠지


if __name__ == "__main__":
    n = 5
    k = 3
    m = 6 #나눌 수
    cnt = 0
   #idx  0  1  2  3  4
    a = [2, 4, 5, 8, 12]
    DFS(0,0,0)

    print(cnt)