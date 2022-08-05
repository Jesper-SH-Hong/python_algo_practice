# 동전 최소로 거슬러줄 방법은?


def DFS(L, sum):
    global res
    if L > res: # 뭐라도 res 찾았으면 그게 최초니 최소 개수일것.. 다음 레벨 뭐하러 가냐 커트!
        return

    if sum > m:  # 커트!!
        return

    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L + 1, sum + a[i])


if __name__ == "__main__":
    a = [1, 2, 5]  # 동전 액면가
    n = len(a)
    m = 15  # 나눠줄 거스름돈

    a.sort(reverse=True)
    res = 2147000000     #최소 찾을 거니까
    DFS(0, 0)

    print(res)  # 사용한 동전 개수! ㅎㅎㅎ
