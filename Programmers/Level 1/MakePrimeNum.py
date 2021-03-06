# 소수 만들기 2021/03/06
# Input
nums = [1,2,7,6,4]

from itertools import combinations
from math import sqrt

def solution(nums):
    nums = map(str,nums)
    nums = list(map("".join, combinations(nums, 3)))
    tmp = []
    sum_n = 0
    
    for n in nums:
        for i in range(len(n)):
            sum_n += int(n[i])
        tmp.append(sum_n)
        sum_n = 0
    print(tmp)
    answer = len(tmp)

    for n in tmp:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                answer -= 1
                break
    
    return answer

print(solution(nums))