n = 9
m = 9  #(문제 수정)기존 코드는 9분짜리 노래를 하나에 담을 수 없음.. 결과를 1로 뱉음..
playtimes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
longest = max(playtimes) ####
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
    if mid >= longest and count(mid) <= m:  #노래 중 가장 긴 노래보다는 dvd 하나의 용량이 크거나 같아야 한다규. 디스크에 무조건 1곡은 담기게.
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)