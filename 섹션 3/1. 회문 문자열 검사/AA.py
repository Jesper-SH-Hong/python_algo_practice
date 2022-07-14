import sys

sys.stdin = open("input.txt", "r")

n = int(input())  # 5

for i in range(n):
    s = input()
    s = s.upper()

    for j in range(len(s)//2):
        if s[j] != s[-j-1]:
            print("#%d No" %(i+1))
            break
    else:
        print("#%d Yes" %(i+1))


    # if s == s[::-1]:
    #     print(f"#{i+1} Yes")
    # else:
    #     print(f"#{i+1} No")
