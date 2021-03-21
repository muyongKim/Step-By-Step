# 소수 찾기 2021/03/21
# Input
numbers = "011"

from itertools import permutations
from math import sqrt

def check(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(num):
    numbers = []
    tmp = ""
    answer = 0

    for i in range(1, len(num)+1):
        per = list(permutations(num, i))
        for n in per:
            for j in range(i):
                tmp += n[j]
            if int(tmp) not in numbers:
                numbers.append(int(tmp))
            tmp = ""

    for n in numbers:
        if check(int(n)):
            answer += 1
    
    return answer

print(solution(numbers))