n = 5
c = 3

a = [1, 2, 8, 4, 9]
a.sort()

res = 0

lt = 1
rt = a[n - 1]


def count(interval):
    cnt = 1  # 배치한 말의 수
    ep = a[0]  # 1번 마굿간에 배치
    for i in range(1, n):
        if a[i] - ep >= interval:  # ep = end point. 기존에 마지막으로 말 배치한 지점과 현재 배치지점의 거리
            cnt += 1
            ep = a[i]

    return cnt

    return n // interval


while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= c:  # 말 여러 마리는 더 들가겠는데요 ㅋㅋ
        res = mid
        lt = mid + 1

    else:
        rt = mid - 1

print(res)
