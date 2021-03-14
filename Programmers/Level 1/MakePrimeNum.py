# 소수 만들기 2021/03/06
# Input
nums = [1,2,7,6,4]

from itertools import combinations
from math import sqrt

def prime_check(total):
    for i in range(2,int(sqrt(total))+1):
        if total % i == 0:
            return False
    return True

def solution(nums):
    nums = list(combinations(nums,3))
    answer = 0

    for n in nums:
        total = n[0] + n[1] + n[2]
        if prime_check(total):
            answer += 1
    
    return answer

print(solution(nums))