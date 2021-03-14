# 멀쩡한 사각형 2021/03/14
# Input
w = 8
h = 12

from math import gcd

def solution(w,h):
    rect = w * h
    answer = 0
    GCD = 0

    if w == h:
        answer = w * h - h
        return answer
    else:
        GCD = gcd(w,h)
        w = w // GCD
        h = h // GCD
        answer = GCD * (w + h - 1)
        return rect - answer

print(solution(w,h))