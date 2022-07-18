

#t = 9010

a = [32, 55, 62, 3700, 250]

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10

    return res

def isPrime(x):   #소수.. 1 주의
    if x == 1:
        return False

    for i in range(2, x//2+1):   #약수는 자신의 1/2까지만 확인하면 다 끝남. 1 x 16   2 x 8  4 x 4...
        if x%i == 0:
            return False
    else:
        return True   # 1, 자신 뺴고 약수가 없네 ㅎㅎ

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')

