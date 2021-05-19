# 이진 변환 반복하기 2021/04/23
# Input
s = '1111111'

def solution(s):
    zero, cnt = 0,0

    while s != '1':
        zero += s.count('0')
        s = ''.join(i for i in s if i == '1')
        s = format(len(s),'b')
        cnt += 1

    return [cnt, zero]

print(solution(s))