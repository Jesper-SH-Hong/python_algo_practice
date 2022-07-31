# DFS는 recursion 갖고 함.

# BFS는 Queue 갖고 추훙헤 배울 것.

# 파이썬에서는 null이 "None"임!!!

# 전위순회 코드 구조:
# DFS():
#    할일
#    D(l)
#    D(r)

# 전위순회: 호출 시작점(루트노드)에서 먼저 일 처리하고, 왼쪽으로 뻗음
# 전위(preorder travers): Root -> L ->R   이렇게 출력                                   1 2 4 5 3 6 7
# 중위(inorder traversal): L -> Root -> R : 왼쪽 leaf까지 갔다가 leaf위 부모 갔다 오른쪽     4 2 5 1 6 3 7
# 후위(postorder travers): L 출력-> R출력 -> Root                                        4 5 2 6 7 3 1

# https://gnujoow.github.io/ds/2016/09/01/DS4-TreeTraversal/
# levelorder = BFS  queue 구조 사용

# 루트의 좌우자식 호출법:
#   1
#  2  3
# 4 5 6 7         #부모값 *2 = L child 값   부모값 *2 + 1 = R child 값


# DFS의 기본구조
# def DFS_1(v):
#     if
#     else:

def DFS_1(v):  # vertex: 꼭지점, 정점
    if v > 7:
        return  # 전체 노드보다 크면 함수 종료해야지.

    else:
        print(v, end=' ')  # 방문(작업)
        DFS_1(v * 2)  # 왼자식 호출
        DFS_1(v * 2 + 1)  # R자식 호출


# def DFS_2(v):  # 중위... 거의 안 쓰임
#     if v > 7:
#         return  #terminate
#     else:
#         DFS_2(v * 2)  # 왼자식 먼저 다 처리
#         print(v, end=' ')  # 부모 처리
#         DFS_2(v * 2 + 1)  # 오른쪽 자식으로


def DFS_3(v):  # 후위  : 병합 정렬!!!!!!!!!!
    if v > 7:
        return  # 55라인으로 가서 종료
    else:
        DFS_3(v * 2)
        DFS_3(v * 2 + 1)
        print(v, end=' ')  # 부모 처리


#   1
#  2  3
# 4 5 6 7         #부모값 *2 = L child 값   부모값 *2 + 1 = R child 값

# stack: D1- D2 - D4 - D8(x)
# stack: D1-D2-D4-D9(X)
# stack: D1-D2(복귀귀점:라인52)-D4
# stack: D1-D2(복귀점:라인53)-D5
# stack: D1-D2-D5-D5-D10(X)

if __name__ == "__main__":
    DFS_1(1)
    print()
    DFS_3(1)
