# 큰 수 만들기
# Input
number = 1924
k = 2

# Stack이 핵심
# Retry
def solution(number, k):
    answer = ''
    number = [int(i) for i in str(number)]
    stack = []
    stack.append(number[0])

    for n in number[1:]:
        while len(stack) > 0 and stack[-1] < n and k > 0:
            k -= 1
            stack.pop()
        stack.append(n)
    
    if k != 0:
        stack = stack[:-k]

    answer = "".join(map(str, stack))
    return answer

print(solution(number, k))