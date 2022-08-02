# 사용하네 안하네로 경우의 수: 상태트리! ㅋㅋ


# 개선안:  result의 "최대값"을 구하는 거니까
# total = 전체 원소합
# tsum = 지금까지의 원소합
# 고민할 아래 레벨들을 다 사용해도 limit에 커버될 거라면
# 더 이상 상태 고민 말고 걍 아래 원소들 다 넣고 끝내면 되지 ㅋㅋㅋ

#          10
#        o/  \x
#       15   15
#     o/    o/      #이렇게 아래 애들은 다 넣는 케이스로 ㅋㅋ total-tsum을 생각
#    17    17
#  o/     o/
# 3      3

def DFS(L, sum, tsum):
    global result
            #total은 업뎃 안할 거니까 global 아님
    if sum + (total - tsum) < result:   #tot - tsum; 확인할 원소들의 합..이 지금 내가 이미 찾은 최적의 답보다 작더라. 고로 아래 자손까진 가지 말자.
        return                          #왼쪽 자식이 o/o/o/o, 케이스라 이미 전체 사례중 왼쪽에 가까운 데서부터 최적값이 나올 것.
    if sum > limit:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L + 1, sum + a[L], tsum + a[L])
        DFS(L + 1, sum, tsum + a[L])

    return result


if __name__ == "__main__":
    limit = 259
    n = 5
    a = [81, 58, 42, 33, 61]
    total = sum(a)

    result = -2147000000
    print(DFS(0, 0, 0))
