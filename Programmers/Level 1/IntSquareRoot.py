# 정수 제곱근 판별 2021/03/05
# Input
n = 121

from math import sqrt

def solution(n):
    if sqrt(n) == int(sqrt(n)):
        return int(pow(sqrt(n)+1, 2))
    else:
        return -1

print(solution(n))