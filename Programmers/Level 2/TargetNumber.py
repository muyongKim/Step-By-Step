# 타겟 넘버 2021/02/21
# Retry
# Input
numbers = [1,1,1,1,1]
target = 3

def solution(numbers, target):
    answer = 0
    stack = [[0,0]]

    while stack:
        index, value = stack.pop()

        if index < len(numbers):
            stack.append([index+1, value - numbers[index]])
            stack.append([index+1, value + numbers[index]])
        else:
            if value == target:
                answer += 1
    
    return answer

print(solution(numbers, target))