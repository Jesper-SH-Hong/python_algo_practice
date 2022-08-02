import sys


# sys.stdin=open("input.txt", "r")

# n =    1      2      3
# sub = o/x -> o/x -> o/x  -> 이렇게 탐색. 총 8가지(공집합 포함)


#             D(1)                                      #이렇게 사용하네/안하네 뻗어나간 게 상태트리
#        o /       \ x
#       D(2)        D(2)
#     o /  \x     o/   \x
#    D(3)
#   o/   \x
#  D(4)   D(4)          ..말단 if문에 걸려 return할 것.
#  1,2,3   1,2


def DFS(v):
    if v == n + 1:              #종착점 v가 말단 노드까지 왔을 떄. 아래와 같이 작업하겠소.
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1     #이값을 사용.
        DFS(v + 1)                          #D1 o->2 o ->3 o ->4
        ch[v] = 0     #이값을 사용 안할래.
        DFS(v + 1)                          #D(3) x -> D(4)


if __name__ == "__main__":
    # n=int(input())
    n = 3
    ch = [0] * (n + 1)  # 어떨떄 사용했나 안했나 확인할 체크 변수.

    DFS(1)

# (릿코드 94. 중위 순회. 참고하셈셈)# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#
#         def DFS(root, res):
#             if root == None:
#                 return
#             else:
#                 DFS(root.left, res)
#                 res.append(root.val)
#                 DFS(root.right, res)
#
#         DFS(root, res)
#         return res