import sys
# sys.stdin = open("input.txt", "rt")


#input은 한 줄씩 끊어서 받음. readline이 더 빠르다고?
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline

# input 커서도 그냥 마지막 읽은 자리에 있나보다.

t = int(input())  # Test cases
for case in range(t):
    n, s, e, k = map(int, input().split())  # 개별 어싸인
    #기초 단계라 복잡성 때문에 변수명 이따구

    a = list(map(int, input().split())) #이러면 공백 split해서 리스트화 이쁘게 됨
    # print(a)

    new_list = a[s-1:e]
    new_list.sort()
    # print("#" + str(case + 1) + " " + str(new_list[k-1]))
    # print("#%d %d" %(case + 1, new_list[k-1]))

    print(f'#{case + 1} {new_list[k-1]}')

