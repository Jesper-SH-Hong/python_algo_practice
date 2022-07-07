a = range(10)
# range (0, 11)
print(list(a))

for _ in range(10):   #_대신 i 해도 되지 ㅋㅋ
    #print("hello")
    pass

for i in range(5, 0, -1):  #(10, 0)은 안됨
    print(i)

print("아래는 while문")
i = 3
while i > 0:
    print(i)
    i -= 1

print("아래는 break")
i = 1
while True:
    print(i)
    if i == 5:
        break        #loop 탈출
    i += 1

print("아래는 for continue")
for i in range(1, 11):
    if i % 2 == 0:
        continue  #아래 body들 무시하고 다음 iteration으로
    print(i)

print("아래는 for else")

for i in range(1, 11):
    print(i)
    if i == 5:
        break
else:           #break 안 걸리고 1~10 정상 종료되면 for문 다돌고 튀나옴. if i>15
    print(11)