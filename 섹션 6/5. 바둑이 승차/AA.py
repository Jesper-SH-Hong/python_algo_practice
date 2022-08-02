#사용하네 안하네로 경우의 수: 상태트리! ㅋㅋ


#개선안:
#total = 전체 원소합
#tsum = 지금까지의 원소합
#고민할 아래 레벨들을 다 사용해도 limit에 커버될 거라면
#더 이상 상태 고민 말고 걍 아래 원소들 다 넣고 끝내면 되지 ㅋㅋㅋ

#          10
#        o/  \x
#       15   15
#     o/    o/      #이렇게 아래 애들은 다 넣는 케이스로 ㅋㅋ total-tsum을 생각
#    17    17
#  o/     o/
# 3      3

def DFS(L, sum):
    global result
    if sum > limit:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L+1, sum + a[L])
        DFS(L+1, sum)

    return result

if __name__ == "__main__":
    limit = 259
    n = 5
    a = [81, 58, 42, 33, 61]


    result = -2147000000
    print(DFS(0, 0))
