#무방향 그래프 <------->방향 그래프(14번)

# <1> --------<2>
# |            |
# |            |
# |            |
# <3>---------<4>-------<5>

# 2차원 배열/리스트로 표현함

# 행, 열 다 각 노드 번호임. 기본적으로 0들로 초기화된 리스트(0 = 간선,연결 없다)
# 항상 출발점이 행. -> 열(도착지)

#graph g  그래프. 인접행렬(2차원 리스트)

# g  1  2  3  4  5
# 1  0  1  0  0  0            1노드(행) ->2노드(열)로 갈 수 있다;
# 2  1  0  0  0  0            2->1도 갈 수 있다.
# 3  0  0  0  0  0
# 4  0  0  0  0  0
# 5  0  0  0  0  0

# g[a][b] = 1
# g[b][a] = 1  양쪽 다 갈 수 있다면 요래 a->b, b->a 다 됨ㅋㅋ.

# 하나씩 읽어나가면서 저렇게 작업하면 됨ㅋㅋ

# g  1  2  3  4  5
# 1  0  1  1  0  0            1노드(행) ->2노드(열)로 갈 수 있다;
# 2  1  0  0  1  0            2->1도 갈 수 있다.
# 3  0  0  0  0  0
# 4  0  1  0  0  0
# 5  0  0  0  0  0

n = 5   #노드 개수
m = 5   #간선 갯수
g = [[0] * (n+1) for _ in range(n+1)]

# 간선 정보
edges = [ [1, 2], [1, 3], [2, 4], [3, 4], [4, 5] ]

for i in range(m):   #2) 출/도착 경로 삽입 (행(정점)->열(정점))
    a, b = edges[i][0], edges[i][1]
    g[a][b]=1
    g[b][a]=1



for i in range(1,n+1):      #1)0 뺴려고 걍 ㅇㅇ. 위 for 문 각주 시 걍 00000 5줄 기본형 뜰것.
    for j in range(1,m+1):
        print(g[i][j], end=' ')
    print()
