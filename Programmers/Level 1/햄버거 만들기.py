# 22.11.12
# https://school.programmers.co.kr/learn/courses/30/lessons/133502
# input
ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]


def solution(ingredient):
    answer = 0
    burger = []

    for i in ingredient:
        burger.append(i)

        if len(burger) >= 4 and burger[-4:] == [1, 2, 3, 1]:
            burger.pop()
            burger.pop()
            burger.pop()
            burger.pop()
            answer += 1

    return answer


print(solution(ingredient))