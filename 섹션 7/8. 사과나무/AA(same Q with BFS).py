
# n이 홀수인 5x5 grid임. [n//2, n//2] 좌표에서 시작하면 됨. 즉 한가운데서 시작

#   0  1  2  3  4
# 0
# 1
# 2       O
# 3
# 4


#    L=0           (2,2)
#          /       |   |     \          dx,dy로 방향 셋업해서 찾자 ㅋㅋ 북부터 시계방향으로
#         /        |   |      \
#      (1,2)    (2,3) (3,2)   (2,1)     L = 1
#     / | | \
#    /  | |  \              남쪽은 이미 방문(남쪽에서 뻗은 거니)했으니 안 감. 체크   (그림 그려보셈)
#                             방문인 즉 그 격자에 적힌 사과수를 더함
#                           같은 이유로  바로 옆가지인  (2,3)은 4가지중 서쪽은 방문 안할 것.


                            # L1이 끝나면 필요한 격자 지역은 다 탐색.
                            # BFS는 이렇게 마름모 꼴로 퍼짐.ㅎㅎ


import sys
from collections import deque

sys.stdin = open("input.txt", 'r')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ch = [[0]*n for _ in range(n)]
sum = 0
dq = deque()
ch[n//2][n//2] = 1
sum += a[n//2][n//2]
dq.append((n//2, n//2))    #튜플쌍으로  que에 넣어놓고
L = 0                      #                        L은 0이다.

while True:
    if L == n//2:  #중앙에서 경계까지 갔다.
        break


    size = len(dq)   #첨엔 1이겠지. (2,2) 있으니. for문이 그 사이즈만큼 돔  // 추후  L = 1일때는 (1,2), (2,3), (3,2) (2,1) 들어서 4개일 거임.
    for i in range(size):
        tmp = dq.popleft()     #그럼 정점(2,2)를 뽑아서 거기서 4가닥 뻗어야 함
        for j in range(4):
            x = tmp[0]+dx[j]  #튜플의 앞놈(x좌표) 떙겨와서 4방향 탐색
            y = tmp[1]+dy[j]

            if ch[x][y] == 0:  #not visited만 갑시다.
                sum += a[x][y]
                ch[x][y] = 1
                dq.append((x,y))

    # print(L, size)
    # for x in ch:
    #     print(x)                      #각주 풀고 프린트하면 레벨별 결과 보임

    L += 1  # i가 현 레벨사이즈를 다 돌았습니다..


print(sum)