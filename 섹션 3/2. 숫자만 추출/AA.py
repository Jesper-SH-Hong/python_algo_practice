s="a012"

# str = ""
# for x in s:
#     if x.isdigit():
#         str += x
#         res = int(str)

res = 0

for x in s:
    if x.isdigit():
        res = res * 10 + int(x)

print(res)

cnt = 0

for i in range(1, res):  #자기 자신도 약수니까..! res//2 노노
    if res % i == 0:
        cnt += 1

print(cnt)
