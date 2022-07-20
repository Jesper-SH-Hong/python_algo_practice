#from collections import deque

n = 5
limit = 140
pax = [90, 50, 70, 100, 60]   #오름차순으로 정렬, 양끝의 가장 무거운 놈에 가장 가벼운 놈을 얹어서 탈주.
                              #안 넘치면 둘 다 탈출, 넘치면 큰 놈만 혼자 태워 탈출



pax.sort()                  #조건: 배에는 최대 두 명만 탑승
# pax = deque(pax)
cnt = 0

while pax:
    if len(pax) ==1:                  #2)그래서 1개만 남았을 때를 위해 이 조건을 추가
        cnt +=1
    if pax[0] + pax[-1] > limit:    #1)주의: 원소 1개 남으면 2배 곱하는 로직..
        pax.pop()
        cnt += 1
    else:
        pax.pop(0)
        # pax.popleft()
        pax.pop()
        cnt += 1

print(cnt)


#리스트: pop(0)시 데이터들을 다 1씩 다 당김.. 비효율적..
#deque 자료형: 첫,끝에서 넣기 뺴기 가능. 중간의 자료들은 이동x. 포인트 변수만 이동.
