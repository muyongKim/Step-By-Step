# 자릿수 더하기 2021/02/04
# Input
n = 123

def solution(n):
    return sum([int(i) for i in str(n)])

print(solution(n))