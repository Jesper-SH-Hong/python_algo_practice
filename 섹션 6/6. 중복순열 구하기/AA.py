# 중복을 허락해서 1,2,3, n개 구슬 중에 m개 뽑는 경우들을 출력해라

# ex 3, 2 -> 1 1, 1 2, 1 3, 2 1, 2 2, 2 3, 3 1, 3 2, 3 3  총 9개

# 즉 n개의 자손/가지가 계쏙 생김ㅋㅋㅋ

# m 크기의 res

#                       D(0)                                    D(L), res[L]=i
#               1/        2|      \3
#               /          |       \          res=[3, ]
#             D(1)       D(2)      D(3)
#            / | \      / | \   1/ 2| \3
#                                 D(2)        res=[3,2]


def DFS(L):
    global cnt
    if L == m:
        for j in res:
            print(j, end=' ')
        print()
        cnt +=1
    else:
        for i in range(1, n+1):
            res[L]=i
            DFS(L+1)


if __name__=="__main__":
    n = 3
    m = 2
    res = [0] * m
    cnt = 0   #갯수
    DFS(0)

    print(cnt)

#트리 그리면서 아래 스택 그려보셈

# |             |                     |             |             |             |
# |             |                     |             |             |             |
# |             |                     |             |             |             |
# |D(2)         | # L==m이니 쾅(팝)     |D(2)         |  pop        |             |                              |D(2)           |  pop
# |D(1)-27, i=1 |                     |D(1)-27, i='2'|             |D(1)-27, i='3'|                             |D(1)-27, i='1' |
# |D(0)-27, i=1 |                     |D(0)-27, i=1 |             |D(0)-27, i=1 |  ....  |D(0)-27, i='2' |      |D(0)-27, i='2' |