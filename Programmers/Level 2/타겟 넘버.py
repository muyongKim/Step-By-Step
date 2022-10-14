# 22.10.14
# https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
# input
numbers = [1, 1, 1, 1, 1]
target = 3

answer = 0


def dfs(depth, total, numbers, target):
    global answer

    # 탈출 조건
    if depth == len(numbers):
        if total == target:
            answer += 1
        return

    # 수행 동작
    dfs(depth + 1, total + numbers[depth], numbers, target)
    dfs(depth + 1, total - numbers[depth], numbers, target)


def solution(numbers, target):
    global answer

    dfs(0, 0, numbers, target)

    return answer

print(solution(numbers, target))