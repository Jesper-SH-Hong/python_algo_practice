len = 10

a = [69, 42, 68, 76, 40, 87, 14, 65, 76, 81]

m = 50

a.sort()
for _ in range(m):
    a[0] += 1
    a[len-1] -= 1
    a.sort()

print(a[len-1] - a[0])