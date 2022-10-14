# 22.10.13
# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# input
s = '()()'


def solution(s):
    answer = True
    stack = []

    if s[0] == ')':
        return False

    for c in s:
        if c == ')':
            if stack:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    if stack:
        answer = False

    return answer

print(solution(s))