# 22.10.27
# https://school.programmers.co.kr/learn/courses/30/lessons/76502
# input
s = "}]()[{"

from collections import deque
from copy import deepcopy


def solution(s):
    answer = 0
    rotate = deque(s)
    i = 0

    while i < len(s):
        stack = []
        tmp = deepcopy(rotate)
        flag = True

        stack.append(tmp.popleft())

        if stack[0] == ']' or stack[0] == '}' or stack[0] == ')':
            rotate.append(rotate.popleft())
            i += 1
            continue

        for c in tmp:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
                continue
            elif not stack:
                flag = False
                break
            else:
                cc = stack.pop()

            if c == ']' and cc == '[':
                continue
            elif c == '}' and cc == '{':
                continue
            elif c == ')' and cc == '(':
                continue
            else:
                stack.append(c)

        if flag and not stack:
            answer += 1

        rotate.append(rotate.popleft())
        i += 1

    return answer

print(solution(s))