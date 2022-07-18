import sys

# sys.stdin = open("input.txt", "rt")

n = int(input())

a = list(map(int, input().split()))

avg = round(sum(a) / n)

min = 2147000000  # 4byte 2^32 /2

#idx = index
for idx, x in enumerate(a):  #리스트의 인덱스/ 밸류 쌍..
    tmp = abs(x - avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1  #nth student

    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1

print(avg, res)


# offset = []
# for j in nums:
#     offset.append(abs(j - avg))     #abs....
#
# print(offset)
#
# candidate_index = []
# for m in range(len(offset)):
#     if offset[m] == min(offset):
#         candidate_index.append(m)
#
# for i in candidate_index:
#     if nums[i] >= avg:
#         print(avg, i+1)
#         break
