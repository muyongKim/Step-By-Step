# 소수 찾기 2021/03/04
# 에라토스테네스의 체
# Input
n = 5

def solution(n):
    checkPrime = [1 for i in range(n+1)]

    for i in range(2,len(checkPrime)):
        if checkPrime[i] == 1:
            idx = 2
            while i * idx <= n:
                checkPrime[i * idx] = 0
                idx += 1
    
    checkPrime[0], checkPrime[1] = 0, 0
    return checkPrime.count(1)
    
print(solution(n))