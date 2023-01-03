# 23.01.03
# https://school.programmers.co.kr/learn/courses/30/lessons/142086
# input
s = "banana"


def solution(s):
    answer = []
    loc = dict()
    front = []

    for i in range(len(s)):
        if s[i] not in front:
            front.append(s[i])
            loc[s[i]] = i
            answer.append(-1)
            continue

        answer.append(i - loc[s[i]])
        loc[s[i]] = i

    return answer


print(solution(s))