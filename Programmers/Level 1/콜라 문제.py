# 23.01.04
# https://school.programmers.co.kr/learn/courses/30/lessons/132267
# input
a = 2
b = 1
n = 20


def solution(a, b, n):
    answer = 0

    while n >= a:
        answer += b * (n // a)
        n = n - a * (n // a) + b * (n // a)

    return answer


print(solution(a, b, n))