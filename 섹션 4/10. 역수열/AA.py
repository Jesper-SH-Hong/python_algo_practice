


n = 8
#x = [4, 8, 6, 2, 5, 1, 3, 7]  solution
a = [5, 3, 4, 0, 2, 1, 1, 0]
seq = [0]*n
filled = 0

for i in range(n):
    for j in range(n):             #a[i]는 자기 자리 전에 넣어야 할 남아있는 큰 수들
        if a[i] == 0 and seq[j] == 0:  #i가 0이다. 그럼 이제 제자리만 찾자. seq[j]에 뭐 있으면 아이쿠; 뭐가 계시군요 지나갑니다.
            seq[j] = i+1
            break
        elif seq[j] == 0:
            a[i]-=1      #빈자리 하나마다 이 a[i]가 작아지니 여기서 앞에 놓일 갯수들은 다 해결될 것.

for x in seq:
    print(x, end=' ')


# 0 0 0 2 0 1 3 0    -> 3앞에 0 4개 잘 깔았음ㅎㅎ seq[j]가 0되는 데가 3의 위치



# 인덱스 헷갈릴 시 꼼수 1)
#range(1,n+1) 하고 seq[j] = i

#꼼수2
# 꼼수 1에 a.insert(0,0) 해서 실제 idx 맞추기