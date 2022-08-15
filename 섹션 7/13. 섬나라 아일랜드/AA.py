# 아파트 단지와 유사함.  차이점은 여긴 북동남서 말고 대각선도 연결로 침. 8방향

from collections import deque
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n = 7
board = [
    [1, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0]
    ]

cnt = 0
q = deque()
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            q.append((i,j))

            while q:                        #얘로 BFS 하나가 끝남. 즉 섬 하나 처리 끝.
                tmp = q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]

                    if 0 <= x < 7 and 0 <= y < 7 and board[x][y] == 1:
                        board[x][y] = 0
                        q.append((x,y))

            cnt += 1  # 섬 갯수 찾는중

print(cnt)




# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, 1, 1, 1, 0, -1, -1, -1]
#
#
# def DFS(x, y):
#     global cnt
#     cnt += 1
#     board[x][y] = 0
#     for i in range(8):
#         xx = x + dx[i]
#         yy = y + dy[i]
#
#         if 0 <= xx < 7 and 0 <= yy < 7 and board[xx][yy] == 1:
#             DFS(xx, yy)
#
#
# if __name__ == "__main__":
#
#     n = 7
#
#     board = [
#         [1, 1, 0, 0, 0, 1, 0],
#         [0, 1, 1, 0, 1, 1, 0],
#         [0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1, 0, 0],
#         [1, 0, 0, 0, 1, 0, 0],
#         [1, 0, 1, 0, 1, 0, 0]
#     ]
#
#     res = []
#
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == 1:
#                 cnt = 0  # 각 단지를 세어야 하므로 누적이 아니라 매 단지 발견시마다 초기화.
#                 DFS(i, j)
#                 res.append(cnt)
#
#     print(res)
