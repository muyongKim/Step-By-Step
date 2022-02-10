# 22/02/10
# String
# Input
s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"

import re

def solution(s):
    nums = re.findall("\d+", s)
    return all(int(nums[i]) < int(nums[i+1]) for i in range(len(nums)-1))

print(solution(s))