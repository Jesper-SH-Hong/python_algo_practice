# 송아지 위치 추적기
# 현수는 +1, -1, +5 이동 가능.
# 최소 몇 번의 점프로 송아지 위치까지 가나

# 시작점 s, 송아지 위치 e.

# BFS
# lvl0       0
#          /  \
# lvl1    1    2
#        / \  / \
# lvl2  3  4  5  6

# 0에서 한번만에 갈 수 있는 것. 1 레벨
# 0에서 두번만에 갈 수 있는 것 2레벨
# 0 1 2 3 4 5 6 순 방문

# BFS를 위한 자료구조는 queue임 FIFO밀어내기.
# 노드값을 넣고, 맨 앞거부터 pop되면, 걔와 연결된, 노드는 모두 queue에 넣음.
# 큐에  들어가면 탐색한다봐야함.

# [0|  | | |....]
#               -> 0 팝, 0 연결된 자식 추가
# [1|2| | | ]
#               -> 1 팝, 1의 자식 추가
# [2|3|4| | ]
#               -> 2 팝, 2의 자식 추가
# [2|3|4| | ]
#               -> 3 팝, 3의 자식 추가
# [3|4|5|6| ]

# 시작점이 5, 도착 14

# dis: 거리 리스트
# 출발해서 몇번만에 그 지점(idx)을 갈 수 있는가.

# idx 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# dis           0

#          5
#        / | \
#       /  |  \   이동가능 경로
#      4   6   10

#              부모
# idx 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# dis         1 0 1        1                출발점 5에서 n번만에 간다.(체크된 건 다시 가지 말 것)

#          5
#        / | \
#       /  |  \
#      4   6   10
#    / | \
#   /  |  \
#   3  5   9
# idx 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# dis       2 1 0 1     2  1                    4가 부모니 4기준에 +1 = 2
#              ..
#              0은 ch 활용할 것. 5는 이미 처음에 방문했으니 걍 방문 말고 0으로 두셈 q에 넣지도 말고.

#이렇게 5 4 6 10 3 5 9 죽죽 하다.. 최초로 14 나오면 끝내면 됨!


#BFS는 출발점이 있고, 최단 거리 탐색. 거리1, 거리 2 ,, 거리 L레벨


from collections import deque

MAX = 10000  #주어진 좌표의 최대값
ch = [0] * (MAX+1) #좌표를 idx로 쓸라니까.. 1부터 쓰게
dis = [0] * (MAX+1)

n = 5   #출발점
m = 14  #목표점

ch[n] = 1   #출발점이니.. 이미 방문했다.
dis[n] = 0  #출발점이니 거리는 출발점으로부터 0

dq = deque()
dq.append(n)

while dq:   #출발점을 추가했으니 비어있진 않음. 비어야 멈출 것. BFS는 비어야 멈춤
    now = dq.popleft()  #now는 현지점
    if now == m:
        break
    for next_ in (now-1, now+1, now+5):   #이러면 저 3갈래로 퍼짐.. 튜플 값을 하나하나 탐색.
        if 0 <next_ <= MAX: #음수 좌표는 없다 ㅐㅎㅆ으니 음수로는 가면 안됨. 좌표는 1부터 10000까지였음
            if ch[next_] ==0:  #방문한 곳이면 탐색하지 말자.
                dq.append(next_)
                ch[next_] = 1
                dis[next_] = dis[now] + 1 # 자기 부모에서 거리 1 추가

print(dis[m])  #몇번 만에 거길 갔을까요?