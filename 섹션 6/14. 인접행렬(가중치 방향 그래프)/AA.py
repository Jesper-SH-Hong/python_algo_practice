#               2            5
#       <1> <------- <2>  ------>  <5>
#         | ------->  /\        /|\
#         |   7   /   |        /
#        4|     /     |      /5
#         |   /  5    |2   /
#        \|/          |  /
#       <3> -------> <4>  <-------  <6>

# node와 간선= 그래프
# 간선 방향 존재 = 방향 그래프
# 간선 값까지 존재 = 가중치 방향 그래프

# intro 보고 오셈(가중치 x 양방향)

# 일단 0으로 초기화,
# 1 2 7  1->2로 가는 건 가중치 7


# g   1  2  3  4  5  6
#     ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 1 | 7  4 ............
# 2 |..................
# 3 |
# 4 |
# 5 |
# 6 |

n = 6  # of vertexes
m = 9  # of edges
edges = [[1, 2, 7],
         [1, 3, 4],
         [2, 1, 2],
         [2, 3, 5],
         [2, 5, 5],
         [3, 4, 5],
         [4, 2, 2],
         [4, 5, 5],
         [6, 4, 5]]

g = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b, c = edges[i][0], edges[i][1], edges[i][2]
    g[a][b] = c


for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()


#저렇게 입력을 따서 출력해보면 인접행렬이 나옴.
# 2->1로 2,  2->3으로 5, 2->5로 5 가중치로 갈 수 있음
