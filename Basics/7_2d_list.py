a = [0] * 3
print(a)

a = [[0]*3 for _ in range(3)]
print(a)
a[0][1] = 1
print(a)

print()

for row in a:
    print(row)

for row in a:
    for col in row:
        print(col, end = ' ')