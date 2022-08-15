# DFS로 풀이함. BFS는 걍 소스코드에 올림. 뭐로 하든 무관.


# 1이 발견된 좌표(0,1)부터 DFS호출을 함. 발견했으면 뻗어나가셈.
# 방문한 보드를 0으로 바꿈!!!!!!! 이 단지 가구수를 세야 하니까. 즉 이미 센 건 0처리

# 백해봤자 다녀온 곳 주위가 다 0이라 깔끔ㅋㅋ

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x,y):
    global cnt
    cnt +=1
    board[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < 7 and 0 <= yy < 7 and board[xx][yy] == 1:
            DFS(xx, yy)


if __name__ == "__main__":

    n = 7

    board = [
        [0, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0]
    ]
    #board = [list(map(int,input())) for _ in range(n)]      -input().split()안 함. 0 1 1..이 아니라 011로 들어와있음 input.txt가


    res=[]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0                 #각 단지를 세어야 하므로 누적이 아니라 매 단지 발견시마다 초기화.
                DFS(i, j)
                res.append(cnt)



    print(res)