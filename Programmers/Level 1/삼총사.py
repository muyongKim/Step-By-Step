# 2022.10.13
# input
number = [-2, 3, 0, 2, -5]

from itertools import combinations


def solution(number):
    answer = 0
    comb = list(combinations(number, 3))

    for n in comb:
        if sum(n) == 0:
            answer += 1

    return answer


print(solution(number))
