# 22.10.27
# https://school.programmers.co.kr/learn/courses/30/lessons/12985
# input
n, a, b = 8, 4, 7

from math import log


def solution(n, a, b):
    front = min(a, b)
    back = max(a, b)
    entry = [_ for _ in range(1, n + 1)]

    while True:
        x = len(entry)
        half = int(x / 2) - 1

        if back > entry[half] and front <= entry[half]:
            return int(log(x, 2))
        elif front > entry[half]:
            entry = entry[half + 1:]
        elif back <= entry[half]:
            entry = entry[:half + 1]

print(solution(n,a,b))