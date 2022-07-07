
n = int(input("숫자를 입력하시오: "))
sum = 0

#n의 약수 구하기
for i in range(1, n+1):
    if n%i == 0:
        print(i, end=' ')   #newline 막지

print()

for i in range(5):
    for j in range(5):
        print(j, end=' ')
    print()

for i in range(5):
    print('i:', i, sep='', end=' ')  #sep으로 print에서, 가 스페이스 안 띄움
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print()

for i in range(5):
    for _ in range(i + 1):   #바디에 _나 j가 없으니 걍 원소 개수만큼 반복
        print("*", end=' ')
    print()

print()

for i in range(5):
    for _ in range(5-i):
        print("*", end=' ')
    print()

print(list(range(5, 0, -1)))