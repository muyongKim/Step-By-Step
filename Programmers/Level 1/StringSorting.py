# 문자열 내 마음대로 정렬하기 2021/02/24
# Input
strings = ["abce","abcd","cdx"]
n = 1

def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x:x[n])
    return strings

print(solution(strings,n))