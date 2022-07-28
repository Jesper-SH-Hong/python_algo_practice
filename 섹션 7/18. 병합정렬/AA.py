# 병합 정렬

# Divide and conquer임. Dsort(Divide & sort 한다 ㅎㅎ)

# 사이즈 8인 어레이가 있으면

#                   D(0,7)
#         D(0,3)              D(4,7)     n//2
#    D(0,1)    D(2,3)    D(4,5)    D(6,7)
# D(0,0) D(1,1) ......
# lt<rt가 아니니.. 0,1 입장에선 위로 가서 합쳐져야 함.

arr = [23,11,45,36,15,67,33,21]

# 원본 리스트 arr에서 작업하는 게 아니라
# tmp에서 작업하고 거기서 복사해서 arr 정렬해야 함.
# arr[p1] , arr[p2] 비교해서
# tmp에 넣고 tmp째로 arr[해당 idx]에 복사해 넣는 거임

# D(0,1)을 반 나누면 각 1개지 0,0  1,1  이미 정렬된 거니까(자기 자신) 합치는 것임.
# 위로 갈수록 자기 일: '이미 정렬된 것들을 합치는' 하겠지

# 그래서 D(0,1)은 끝내고 D(0,3)을 들러 내려가서 D(2,3)을 할 것.
# 그렇게 두 자식 다 끝나니 D(0,3)이 본연의 일을 할 것. 둘 합치기
# 그럼 p1은 idx 0  p2는 idx 2 가리키게 해서 병합 [11,23]  vs [36,45]

# 11과 36 하니 11
# [11, ?, ?, ?]

# 23과 36 비교하니 23
# [11, 23, ?, ?]

        # 0   1   2   3   4   5   6    7
# arr = [11, 23, 36, 45, 15, 67, 33, 21]  #그 결과 이렇게 될 것.

#이렇게 D(0,3)이 끝났으면
#D(0,7)이 아직 처리 안하고 D(4,7) 해결 기다릴 것.

#D(4,7)의 결과 아래와 같을것
#    [11,23,36,45,     15,21,33,67]
# tmp [ 작은거부터 비교해서 넣기    ]



def Dsort(arr, lt,rt):
    if lt<rt:
        mid=(lt+rt)//2
        Dsort(arr, lt, mid)
        Dsort(arr, mid+1, rt)

        #ㅇㅋ 위에서 좌,우 children 다 처리되서 돌아왔으면 마무리 일을 아래와 같이 하자.

        p1=lt  # part. 왼쪽 덩어리를 컨트롤     p2는 중간 담부터 컨트롤,   그리고 나서 tmp에 넣기
        p2=mid+1
        tmp= []
        while p1<= mid and p2 <=rt:  #하나라도 끝을 넘어가면 멈춰야.
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1

        if p1 <= mid:
            tmp = tmp + arr[p1:mid+1]
        if p2 <= rt:
            tmp = tmp + arr[p2:rt+1]

        for i in range(len(tmp)):    #주의: 만약 D(4,7)이면 tmp의 idx가 0,1,2,3이어도 arr엔 4,5,6,7 가야겠지 ㅋㅋㅋ
            arr[lt+i] = tmp[i]







if __name__ == "__main__":
    arr = [23,11,45,36,15,67,33,21]
    print("Before sort: ", end='')
    print(arr)
    Dsort(arr, 0, 7)
    print()
    print("After sort: ", end='')
    print(arr)