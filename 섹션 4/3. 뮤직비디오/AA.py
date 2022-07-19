n = 9
m = 3
playtimes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lt = 1
rt = sum(playtimes)  # 45     9곡을 1장에 담으면 45분.. 길지만 답은 되겠지 ㅋㅋㅋ

# bin search로 dvd 용량의 최소치를 찾아보자..

# 1+45  //2  = mid: 23  -> 1~6/  7 8 / 9   3장.
# res => 23

# 1~ 22 => mid: 11  ->  1 2 3 4 / 5 6 / 7 / 8 / 9... 5장 에바..

# 12~ 22 -> 17 ->   1~5/ 6,7/ 8,9  => 3장
# res = 17


res = 0


def count(disc_capa):
    cnt = 1  # discs
    sum = 0  # total music length in current disc
    for x in playtimes:
        if sum + x > disc_capa:
            cnt += 1  # 새로 1장 필요하겠네
            sum = x  # 첫곡

        else:
            sum += x

    return cnt


while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) <= m:  # 만약 결과가 2? 오 2장으로 되면 3장에도 쌉가능이니 ㅋㅋ
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)