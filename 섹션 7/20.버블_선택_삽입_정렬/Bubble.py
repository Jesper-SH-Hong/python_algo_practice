# 1) Bubble sort   - compare adjacent elems...
# idx0, 1 비교
# idx1, 2 비교
# 이런 식으로 죽죽... 하다 보면 첫 iteration에선 맨 뒤에 가장 큰 수 놓임(사이의 정렬은 모름)
#
#
#
# 1회차
# [3,2,1]  -0,1
# [2,3,1]  -1,2
# [2,1,"3"]
#
# 2회차
# [1,"2",3]  -0,1       뒤에서 두번쨰도 제값을 찾음.
#

def bubbleSort(s):
    for i in range(len(s) - 1):  # 알고리즘의 총 시도 횟수  idx 0부터, n-1까진 해볼것
        swap = False  # 한번이라도 작동 여부 확인

        for j in range(len(s) - 1 - i):  # 각 시도는 맨 마지막부터 한 elem씩 정렬 상태로 만듦.
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
                swap = True

        if not swap:
            break

    return s


print(bubbleSort([5, 1, 4, 3, 2]))

#O(n^2)
#worst: n(n-1)/2
#Best: O(n) 이미 정렬되서 한번 훌틱만.