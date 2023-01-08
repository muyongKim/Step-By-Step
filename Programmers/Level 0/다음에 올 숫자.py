# 23.01.08
# https://school.programmers.co.kr/learn/courses/30/lessons/120924
# input
common = [1,2,3,4]


def solution(common):
    answer = 0

    minus = common[1] - common[0]

    if common[0] == 0 or common[1] == 0:
        division = 1
    else:
        division = common[1] // common[0]

    if (common[2] - common[1]) == minus:
        answer = common[-1] + minus
    else:
        answer = common[-1] * division

    return answer