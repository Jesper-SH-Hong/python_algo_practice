import sys

sys.stdin = open("input.txt", "r")

n = 5
matrix = []

# for _ in range(n):
#     a = [list(map(int, input().split())) for _ in range(n)]
#     matrix += a

# print(matrix)
#
# row_sums = [0] * n
# col_sums = [0] * n
# pos_diag_sums = 0
# neg_diag_sums = 0
#
# for i in range(n):
#     for j in range(n):
#         row_sums[i] += matrix[i][j]
#         col_sums[j] += matrix[i][j]
#     pos_diag_sums += matrix[i][n - i - 1]
#     neg_diag_sums += matrix[i][i]
#
# print(max(max(row_sums), max(col_sums), pos_diag_sums, neg_diag_sums))

a = [list(map(int, input().split())) for _ in range(n)]

largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]  # 옼ㅋㅋ 그냥 각 열과 각 행의 합을 바로 매번 비교
        if sum1 > largest:
            largest = sum1
        if sum2 > largest:
            largest = sum2

sum1 = sum2 = 0
for i in range(n):             # 한줄에 한 값씩만 더하며 내려오면 될테니...
    sum1 += a[i][i]
    sum2 += a[i][n - i - 1]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

print(largest)
