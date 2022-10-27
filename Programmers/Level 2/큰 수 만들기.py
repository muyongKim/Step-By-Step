# https://school.programmers.co.kr/learn/courses/30/lessons/42883
# Input
number = '1924'
k = 2

# 21.01.21
# def solution(number, k):
#     answer = ''
#     number = [int(i) for i in str(number)]
#     stack = []
#     stack.append(number[0])
#
#     for n in number[1:]:
#         while len(stack) > 0 and stack[-1] < n and k > 0:
#             k -= 1
#             stack.pop()
#         stack.append(n)
#
#     if k != 0:
#         stack = stack[:-k]
#
#     answer = "".join(map(str, stack))
#     return answer

# 22.10.28
def solution(number, k):
    number = list(number)
    stack = [number[0]]

    for n in number[1:]:
        while stack and k != 0 and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)

    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)


print(solution(number, k))