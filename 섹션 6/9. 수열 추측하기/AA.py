# n개의 정수
# 두 인접수의 합이 다음줄로
# 3 1 2 4
#  4 3 6
#   7 9
#   16    f


# 꼼수인 규칙이 있음.
# 1       2       3       4
#   1+2      2+3     3+4
#     1+2+2+3  2+3+3+4
#        1+2*3+3*3+4
#          3C2 3C2    <- n이 4일때 1 3 3 1

# (파스칼 삼각형. 검색해보셈ㅋㅋㅋ)

# 즉, 계속 1+1같이 시뮬레이션 돌리면 엄청 비효율적일테니
# 1 3 3 1  nCr을 미리 만들고
# 1 2 3 4  이렇게 서로 곱해주면 되지 않을까

# n = 5 -> 4C0 4C1 4C2 4C3 4C4


# 즉, 순열을 다 뽑아내놓고 각 순열 케이스들을 nCr이랑 곱해서 맞는 놈을 구하며 노디지 않을까.


def DFS():


if __name__ == "__main__":
    n = 4
    f = 16  # final
    p = [0] * n
    b = [1] * n  #이항계수 미리 초기화 nCr.  어차피 양끝은 1일테니 1로 초기화
    ch = [0] * (n + 1)   #순열 생성용 중복 체커

    # nCr의 구현: nPr / r!        = n! / [(n-r)! X r!]
    # idx  0    1    2      3
    # b    1    1    1      1

    #          3C1  3C2    3C3

    #     1*3   3   3x2'  `3x2x1
    #     ---  ---  ---   ------
    #      1    1  '2*1  '3*2*1

    # b    1    3    3      1

    for i in range(1, n):
        b[i] = b[i-1] * (n-1) / i

