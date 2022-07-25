import sys

sys.stdin = open("input.txt", "r")

board = [list(map(int, input().split())) for _ in range(7)]

     0 1 2 3 4 5 6
0  <| | | | | |>|
1   | | | | | | |
2   | | | | | | |
3   | | | | | | |
4   | | | | | | |
5   | | | | | | |
6   | | | | | | |

cnt = 0
for i in range(3):   #사이즈가 5인 palindrome을 찾으니 그냥 종/횡 다 0,1,2에서만 시작하면 됨.

    #행처리
    for j in range(7): #7행
        tmp=board[j][i:i+5]   #j는 행. i는 5개를 솎아내는 역할
        if tmp ==tmp[::-1]:
            cnt+=1

        #열처리
        for k in range(2): # 회문 길이 5니까 5//2만 체크.    세로..는 이렇게
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt+=1


print(cnt)