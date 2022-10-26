# 숫자의 표현 기22.10.27
# https://school.programmers.co.kr/learn/courses/30/lessons/12924
# Input
n = 15

# 21.02.21
# def solution(n):
#     answer = 0
#     start = 1
#     tmp = 0
#
#     while start <= n:
#         for i in range(start, n+1):
#             tmp += i
#             if tmp == n:
#                 answer += 1
#                 tmp = 0
#                 break
#             elif tmp > n:
#                 tmp = 0
#                 break
#         start += 1
#     return answer

def solution(n):
    answer = 0

    for i in range(1, n + 1):
        tmp = 0

        while tmp < n:
            tmp += i

            if tmp == n:
                answer += 1
                break
            i += 1

    return answer

print(solution(n))