# 정수 내림차순으로 배치하기 2021/02/05
# Input
n = list(input())

def solution(n):
    n.sort(reverse=True)
    return int("".join(n))

print(solution(n))