import itertools
import sys

sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
nums = list(map(int, input().split()))
# sum_list = []
#
# selected_nums = list(itertools.combinations(num_list, 3))
#
# for tuple_ in selected_nums:
#     sum_list.append(sum(tuple_))
#
# x = set(sum_list)
# y = list(x)
# y.sort()
#
# print(y[-k])

sums_set = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            sums_set.add(nums[i] + nums[j] + nums[m])

sums_set = list(sums_set)
sums_set.sort()
sums_set.reverse()

print(sums_set)
print(sums_set[k-1])

