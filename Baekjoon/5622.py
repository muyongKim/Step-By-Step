# 다이얼 2021/06/03
# 분류 : 구현

word = input()

time = 0
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for w in word:
    for d in dial:
        if w in d:
            time += dial.index(d) + 3

print(time)