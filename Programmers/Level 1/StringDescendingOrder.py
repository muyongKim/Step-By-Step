# 문자열 내림차순으로 배치하기 2021/03/01
# Input
s = "Zbcdefg"

def solution(s):
    s = list(s)
    s.sort(reverse = True)
    return "".join(s)

print(solution(s))