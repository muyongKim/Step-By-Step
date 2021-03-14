# 멀쩡한 사각형 2021/03/14
# Input
w = 8
h = 12

from math import gcd

def solution(w,h):
    answer = 0

    if w == h:
        answer = w * h - h
        return answer
    else:
