# 딕셔너리는 키(idx)로 정수 외에 글자, 단어도 됨.
# 밸류를 다 1로 떄렸다가 다 0으로 바꾸면 1로 딱 살아있는 게 답이겠지.


a = ["big", "good", "sky", "blue", "mouse"]
b = ["sky", "good", "mouse", "big"]

dic = dict()

for x in a:
    dic[x] = 1

for y in b:
    dic[y] = 0

for key, val in dic.items():
    print(key, val)
    if val == 1:
        print(key)
        break
