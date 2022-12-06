# 22.12.07
# https://school.programmers.co.kr/learn/courses/30/lessons/134240
# input
food = {1, 3, 4, 6}


def solution(food):
    answer = ''

    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)

    answer += '0' + answer[::-1]

    return answer


print(solution(food))