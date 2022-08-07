#조합
#1~n 사이에서 m개의 숫자를 뽑는다.
#DFS(레벨, 뽑을 번째)
#상태 트리 해서 res[0], res[1]에 넣기.

#                 D(0,1)
#        1/    2|    3|    \4
#     D(1,2)             D(1,5)(X)   ->     시작도 못하고 죽음. 4까지만 돌리래는데 시작이 5 ㅋㅋ
#    2/ 3| \4    - 이미 들어간 놈 다음 숫자부터 돌림
# D(2,3)         - 말단이니 리턴

                    # idx       0  1       0  1
                    # res[L] = [1, 2]  -> [1, 0] -> [1,3] ... [2,3] -> [2,0] ->[2,4]...
                    #           말단       D(1,2)   다시 말단

def DFS(L, s):
    global cnt
    if L == m:
        for j in res:
            print(j, end=' ')
        cnt+=1
        print()
        return
    else:
        for i in range(s, len(n)+1):
            res[L] = i
            DFS(L+1, i+1)    #굳이 res에 뭐가 들어갔는지 체크 안해도 이렇게 앞에 넣은 거 다음부터 죽 돌려주면 된다.
            res[L] = 0

if __name__ == "__main__":
    n = [1, 2, 3, 4]
    m = 2
    res = [0] * m
    cnt = 0
    DFS(0, 1)

