# 매 시도마다 가장 작은 원소를 찾아서 앞으로 뺌
# 반복할수록 앞에서 1칸씩 뒤까지 정렬이 되어나갈 거임.
# 가장 작은 값을 선택해서 선택 정렬이라 함.

# [9,1,2,7]
# ["1",9,2,7]
# [1,"2",9,7]
# [1, 2, "7", 9]
# [1, 2, 7, 9]

# n번의 시도가 있겠고..   , 앞에서 i만큼 띄워서 작업해나가게 ㅗ디겠네


def selectionSort(s):
    for i in range(len(s) - 1):
        swapped = False

        for j in range(i, len(s)):
            min_num = 1000000000
            if s[j] < min_num:
                min_num = s[j]
                min_idx = j

            s[i], s[j] = s[j], s[i]
            swapped = True

        if swapped == False:
            break

    return s


print(selectionSort([5, 4, 3, 2, 1]))


def selectSort(s):
    for i in range(len(s) - 1):
        min_idx = i

        for j in range(i + 1, len(s)):
            if s[j] < s[min_idx]:
                min_idx = j

        s[i], s[min_idx] = s[min_idx], s[i]

    return s


print(selectSort([7, 4, 3, 1]))


text = "  hi bi  ci   di "
t2 = text.strip().split()
print(t2)