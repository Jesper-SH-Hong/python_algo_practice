n = [1, 2, 3, 5]

m = [3, 7]

i =j = 0
res = []


while i < len(n) and j < len(m):
    if n[i] <= m[j]:
        res.append(n[i])
        i += 1

    else:
        res.append(m[j])
        j += 1

if i < len(n):
    res = res + n[i:]
if j < len(m):
    res = res + m[j:]

print(res)
