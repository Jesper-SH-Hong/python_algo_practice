import sys

# sys.stdin=open("input.txt", "r")

# n개의 원소인 자연수 집합
# 두 부분집합을 나눠서 합이 같은 경우가 있으면 YES, 아니면 NO 출력


# 1을 부분집합에 넣는다/만다
# 3을 ...

# 토탈 2 **6 -1(공집합) 경우의 수


a = 1, 3, 5, 6, 7, 10


# DFS(L, sum)   #L:a의 인덱스 번호이자 동시에 Level   #sum: 부분집합의 합

# idx 0  1  2  3  4  5
# a = 1, 3, 5, 6, 7, 10

#                 D(0,0)
#               /       \
#           D(1,1)      D(1,0)        왼쪽: 0번인덱스(값:1)을 부분집합에 사용 <-> 오른쪽: 안사용
#            /  \        /  \
#      D(2,4)   D(2,1)                  sum: 1+3   vs  1
#      /   \
# D(3,9)   D(3,4)                     #역시 끝은 L이 n이 되어야 끝날 것.(idx 0부터 시작했으니 5레벨까지 n레벨 채워지고  6레벨(n)에 도달해야 leaf)


def DFS(L, sum2):
    if sum2 > total // 2:         #없어도 무관이지만, 시간복잡도 줄이기. (아, 아예 total이 홀수냐고 물어봐도..?)
        return
    if L == n:   #6렙 도달
        if sum2 == (total - sum2):  # 부분집합1에 참여하지 않은 원소들의 합, 즉 부분집합2의 합이랑 같냐.
            print("YES")
            sys.exit(0) #플그램 종료
    else:
        DFS(L + 1, sum2 + a[L])
        DFS(L + 1, sum2)


if __name__ == "__main__":
    # n = int(input())
    # a = list(map(int, input().split()))
    n = 6
    a = [1, 3, 5, 6, 7, 10]
    total = sum(a)
    DFS(0, 0)
    print("NO")
