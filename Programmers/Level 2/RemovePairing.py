# 짝지어 제거하기 2021/02/23
# Input
s = "cdcd"

def solution(s):
    s = list(s)
    index = 0

    while s:
        if index == len(s)-1:
            return 0

        if s[index] == s[index+1]:
            s.pop(index)
            s.pop(index)
            index = -1
        index += 1

    return 1

solution(s)