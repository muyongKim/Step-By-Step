# 피보나치 수 2021/05/01
# Input
n = 3

def solution(n):
    fibonacci = [0,1]
    num = 0

    for i in range(2,n+1):
        num += fibonacci[i-2] + fibonacci[i-1]
        fibonacci.append(num)
        num = 0
    
    return fibonacci.pop() % 1234567

print(solution(n))