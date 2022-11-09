# 22.11.10
# https://school.programmers.co.kr/learn/courses/30/lessons/133501#
# input
distance, scope, times = 10, [[7,8],[4,6],[11,10]], [[2,2],[2,4],[3,3]]


def solution(distance, scope, times):
    answer = distance

    for s in scope:
        s.sort()

    for i in range(len(scope)):
        for j in range(scope[i][0], scope[i][1] + 1):
            if 1 <= (j % sum(times[i])) <= times[i][0]:
                if answer > j:
                    answer = j

    return answer


print(solution(distance, scope, times))