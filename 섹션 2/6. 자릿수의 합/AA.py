import sys

# sys.stdin = open("input.txt", "rt")
# n = int(input())
# a = map(int(input().split()));

n = 3
a = [125, 15232, 97]
sol = []


def digit_sum(x):
    sum = 0
    # while x > 0:
    #     sum += x % 10
    #     x = x // 10
    #
    # return sum

    for i in str(x):
        sum += int(i)
    return sum

max_ = -2147000   # C++ int = 4byte = - 2^31 ~ 2^ 31-1 ( 0 포함)

for x in a:
    tot = digit_sum(x)
    if tot > max_:
        max_ = tot
        res = x

print(x)

