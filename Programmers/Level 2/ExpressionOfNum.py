# 숫자의 표현 2021/02/21
# Input
n = 15

def solution(n):
    answer = 0
    start = 1
    tmp = 0
    
    while start <= n:
        for i in range(start, n+1):
            tmp += i
            if tmp == n:
                answer += 1
                tmp = 0
                break
            elif tmp > n:
                tmp = 0
                break
        start += 1
    return answer

print(solution(n))