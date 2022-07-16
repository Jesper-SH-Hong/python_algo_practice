n = 5

a = [
    [10, 13, 10, 12, 15],
    [12, 39, 30, 23, 11],
    [11, 25, 50, 53, 15],
    [19, 27, 29, 37, 27],
    [19, 13, 30, 13, 19],
]
mid_idx = n // 2
sum = 0
for i in range(mid_idx + 1):
    sum += a[i][mid_idx]
    if i != 0:
        for j in range(1, i + 1):
            sum += a[i][mid_idx + j]
            sum += a[i][mid_idx - j]

for i in range(n-1, mid_idx, -1):
    sum += a[i][mid_idx]

    if i != n-1:
        for j in range(1, n - i):
            sum += a[i][mid_idx + j]
            sum += a[i][mid_idx - j]

print(sum)