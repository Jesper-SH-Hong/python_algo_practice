def check(a):
    for i in range(9):
        ch1 = [0] * 10  # ch = check
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False

    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[3 * i + k][3 * j + s]] = 1

            if sum(ch3) != 9:
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("Yes")
else:
    print("No")
