# DFS니 역시 상태 트리 그리고 시작하겠음.  DFS 문제 같다 싶으면 상태 트리만 잘 그리면 끝남 ㅎㅎ
# n개의 동전을 3사람에게 분배해서 사람 간 보유 동전합이 차이가 최소가 되게 해라(단 서로 달라야 함?)


# n = 7
# coins = [8, 9, 11, 12, 23, 15, 17]

# 동전 8을 사람 A,B,C, 누구에게 줄래
# 각 사람이 받은 동전합은 money란 리스트에 업뎃해주자

# money = [0] * 3

#                D(L)
#              /  |  \
#            0/  1|  2\      동전을 이 사람(가지 번호) 에게 분배하겠다.
#            D(L)            money = [8]
#           /  |  \
#         0/ 1 |  2\         만약 이번 동전(9)는 1이란 놈 한테 줬다?
#            D(L)                              money= [8,9,0]
#            /  | \
#         0 / 1 | 2\
#         D(L)                money = [19,9,0]       주의점은 다시 backtracking할 때
#                                                    그 인간한테 안 준 걸로 처리하려면 money[i]에서 동전값을 빼줘야함
#                                                    옆 가지 가기 전 윗가지 money = [8,9,0]

def DFS(L):
    global res
    if L == 7:
        diff = max(money) - min(money)
        if diff < res:
            tmp = set(money)                #각 사람의 동전합은 다 달라야 함.
            if len(tmp) == 3:
                res = diff
                                    #return 필요 없음. DFS 돌던중임ㅋㅋㅋ

    else:
        for i in range(3):
            money[i] += coins[L]
            DFS(L+1)
            money[i] -= coins[L]   #백, 풀어주기!
            # DFS(L+1) .. 뭐하냐 for문 돌리는데;;;  o/x 상태트리나 그렇게 해야지.. for문 없으니..


if __name__ == "__main__":
    n = 7
    coins = [8, 9, 11, 12, 23, 15, 17]
    money = [0] * 3
    res = 2147000000
    DFS(0)
    print(res)