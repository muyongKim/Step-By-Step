# 23.01.07
# https://school.programmers.co.kr/learn/courses/30/lessons/120923
# input
num = 3
total = 12


def solution(num, total):
    answer = []
    first_int = (total - ((num - 1) * num) // 2) // num

    for i in range(num):
        answer.append(first_int + i)

    return answer


print(solution(num, total))