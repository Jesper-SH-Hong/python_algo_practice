#     0   1   2   3
# ch  0   1   0   0


def DFS(L):
    global res
    # global ch   ch=[~~]가 아니니  사실 위아래 둘다 없어도 돔.
    if L == m:
        global cnt
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                res[L] = i
                ch[i] = 1
                DFS(L + 1)
                ch[i] = 0  # !!!!!!!!!! 되돌려주기. 그림 그려보셈. 라인 19와 대칭. DFS(L+1)을 갔다 DFS(L)로 되돌아온 것.


if __name__ == "__main__":
    n = 3
    m = 2
    ch = [0] * (n + 1)
    res = [0] * m
    cnt = 0  # 전체 개수를 구하시옹
    DFS(0)

    print(cnt)
