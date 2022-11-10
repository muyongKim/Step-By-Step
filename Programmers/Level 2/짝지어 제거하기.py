# 22.11.11
# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# input
s = 'baabaa'


def solution(s):
    stack = []

    for c in s:
        if stack:
            if stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()
        else:
            stack.append(c)

    return 0 if stack else 1


print(solution(s))