#탑다운. 재귀/ 메모이제이션

#dy=[0,0,0...]으로 초기화해놓고 넣으셈


#                D(7)   7m를 자르는 방법의 수  -앞서 봤듯 꼬다리 1일때 DFS(6), 꼬다리 2일떄 DFS(5)
#              /     \
#           D(6) + D(5)
#         /   \
#       D(5) + D(4)
#       /   \           아래 찍고 올라와서 D(4) 뻗을 필요 없어짐..
#      D(4) D(3)
#     /  \   / \   여긴 뻗을 필요 없음 이미 왼쪽 아랫단에서 하고 기록해두었으므로
#   D(3)+D(2)
#  /  \
#D(2) D(1)   #직관적으로 파악 가능한 길이
# 2    1      #L이 2나 1이면 각각 그걸 리턴하게 설계


# 재귀 돌릴 떄 이미 구해진 걸 기록해서  똑같은 게 나올 떈 cut edge하는 게 메모이제이션임. 불필요한 재귀호출 방지.


def DFS(len):
    if dy[len] > 0:      #final. cutting edge. leaf까지 뻗지 말고 걍 그거 리턴해버려라.
        return dy[len]
    if len == 1 or len ==2:
        return len
    else:
        # return DFS(len-1) + DFS(len-2)    이대로도 답은 나옴

        dy[len] = DFS(len-1) + DFS(len-2)  #1)메모이제이션. 아직 가지 컷은 안함
        return dy[len]                      #메모이제이션을 하므로 Dynamic programming임. 이거 없으면 걍 recursion임..

if __name__ =="__main__":
    n = 7
    dy= [0]* (n+1)   #메모이제이션 용
    print(DFS(n))



