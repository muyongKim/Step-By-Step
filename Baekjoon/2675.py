# 문자열 반복 2021/06/06
# 분류 : 구현, 문자열

t = int(input())

answer = []
for i in range(t):
    p = ''
    r, s = input().split()
    for char in s:
        p += char * int(r)
    answer.append(p)

for a in answer:
    print(a)