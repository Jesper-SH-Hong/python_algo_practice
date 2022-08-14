# 문제 요구: 미로 탈출의 가지수. 최단 거리를 찾는 게 아님
# DFS로 cnt 세알려야 함.   한번에 쭉 가서 도착하고, 다시 뺵해서 다른 경로로 쭉 가고...            BFS는 동심원, DFS는 쭉 뻗었따 뺵했다임.
# 빽 시에 체크 풀어주는 거 잊지말기


n = 7

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt

    if x == n-1 and y == n-1:
        cnt += 1

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < n and 0 <= next_y < n and board[next_x][next_y] == 0:
            board[next_x][next_y] = 1    #방문할 곳 벽으로 방문 처리(체크해버려).
            DFS(next_x, next_y)
            board[next_x][next_y] = 0    #뒷자리로 돌아와서 방금 다녀온 가지 풀어주기.


if __name__ == "__main__":
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0]
    ]

    cnt = 0

    board[0][0] = 1
    DFS(0, 0)
    print(cnt)
