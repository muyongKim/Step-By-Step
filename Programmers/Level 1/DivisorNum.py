# 약수의 개수와 덧셈 2021/05/18
# Input
left, right = 24, 27

from math import sqrt

def solution(left,right):
    answer = 0

    for n in range(left, right+1):
        if sqrt(n) == int(sqrt(n)):
            answer -= n
        else:
            answer += n
    
    return answer

print(solution(left,right))