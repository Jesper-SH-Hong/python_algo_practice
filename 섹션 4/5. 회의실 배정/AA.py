import sys

sys.stdin = open("input.txt", 'r')
n = int(input())
meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))  # tuple

# meeting.sort() # 참고: 튜플도 앞자리 기준으로 정렬됨
meeting.sort(key=lambda x: (x[1], x[0]))  # x[1]이 최우선 기준, x[0]이 차우선 기준으로 정렬해라. 즉 끝타임 기준으로.
# key는 기준
print(meeting)

et = 0  # end time
cnt = 0 # 회의수
for s, e in meeting:
    if s >= et:
        et = e
        cnt +=1

print(cnt)
