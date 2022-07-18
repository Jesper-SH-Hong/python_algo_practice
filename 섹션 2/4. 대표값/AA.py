import sys

# sys.stdin = open("input.txt", "rt")

n = int(input())

a = list(map(int, input().split()))

#avg = round(sum(a) / n) # 파이썬 round = round_half_even 방식 = 정확히 half 지점이면 even(짝수)값으로 근사를 취함. 4와 5 사이면 4로 ㅎㅎ
                        #   round(a)= 4.500 0 -> 4       4.5111 -> 5
                        #   5.5   -> 6(even)
                        # round_half_up 방식으로 해야 함..


#d =66.4, 66.5, 66.9
#d = a + 0.5     // 66.9  67  67.4
#d = int(d)      //66 67 67

avg = int(sum(a)/n + 0.5)


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
