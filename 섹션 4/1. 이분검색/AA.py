# 이분 검색
# 양 끝에 lt,  rt 인덱스, mid라는 중간 지점 변수 이용

# ex. "32" 찾기

# 8개의 원소(정렬된 상태)
#  0  1   2   3   4   5   6   7
# [12, 23, 32, 57, 65, 81, 87, 99]

# mid = (lt+rt)//2      =  3 (idx)

# a[mid] == m이면 개이득

# goal < a[mid] 이면 왼쪽 절반에서 다시 search
# rt = mid-1
# 그럼 0~2 인덱스만 체크. 다시 mid를 보면
# mid = 2//2 = 1
# a[mid] = 23

# 그럼 이젠 작은 쪽 버리게 lt = mid + 1

# 이제 mid는 (2+2)//2  \ 1
# a[2]
# 2+ 1 = 3

# log_2 N번만에 다 찾을 수 있음.


n = 8
m = 32

a = [23, 32, 12, 65, 99, 81, 87]

a.sort()  # !!
lt = 0
rt = n - 1

while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid - 1

    else:
        lt = mid + 1
