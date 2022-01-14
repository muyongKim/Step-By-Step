# 나머지가 1이 되는 수 찾기 2022/01/14
# Input
n = 36

def solution(n):
    for i in range(2, n):
        if (n-1) % i == 0:
            return i

print(solution(n))