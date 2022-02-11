# 22/02/11
# Array, Enumeration
# Input
nums = [3,3,6,4,5]

from itertools import combinations

def solution(nums):
    output = 0
    comb = list(combinations(nums,4))

    for n in comb:
        if sum(n[:3]) == n[3]:
            output += 1
    return output

print(solution(nums))