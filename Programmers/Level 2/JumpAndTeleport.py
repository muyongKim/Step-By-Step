# 점프와 순간 이동 2021/03/23
# Input
n = 6

def solution(n):
    answer = 0

    while n != 0:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            answer += 1

    return answer

print(solution(n))