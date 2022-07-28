# 이 환자가 몇번쨰 진료를 받을까?
# 제일 첫 환자는 0
# N명의 환자가 있고, 환자 리스트상 인덱스가 M인 환자가 몇번쨰로 진료를 받을까?
# 위험도에 따라 진료를 받게 됨.

# sorting하면 안되냐? => 중복이 있으면..?
# 60 60 90 60 60 60의 경우에는 60인 환자면 곤란하지.


from collections import deque

n = 5
m = 2

a = [60, 50, 70, 80, 90]

q = [(pos, emergency) for pos, emergency in enumerate(a)]

print(q)

q = deque(q)
cnt = 0

while True:
    cur = q.popleft()
    if any(cur[1] < x[1] for x in q):
        q.append(cur)
    else:
        cnt+=1
        if cur[0] == m:
            print(cnt)
            break