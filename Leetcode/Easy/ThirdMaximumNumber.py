# 22/02/14
# Array, Sorting
# Input
nums = [1,2]

def solution(nums):
    nums = list(set(nums))
    nums.sort(reverse=True)

    if len(nums) >= 3:
        return nums[2]
    else:
        return nums[0]

print(solution(nums))
# Runtime: 80 ms, faster than 39.43% of Python3 online submissions for Third Maximum Number.
# Memory Usage: 15.4 MB, less than 35.40% of Python3 online submissions for Third Maximum Number