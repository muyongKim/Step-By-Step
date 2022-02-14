# 22/02/14
# Array, Greedy, Sorting
# Input
nums = [2,-3,-1,5,-4]
k = 2

def solution(nums, k):
    nums.sort()

    for i in range(len(nums)):
        if k == 0 or nums[i] >= 0:
            break
        nums[i] = - nums[i]
        k -= 1

    output = sum(nums)

    if k % 2 == 1:
        output -= min(nums)*2

    return output

print(solution(nums, k))
# Runtime: 48 ms, faster than 88.21% of Python3 online submissions for Maximize Sum Of Array After K Negations.
# Memory Usage: 14.1 MB, less than 76.29% of Python3 online submissions for Maximize Sum Of Array After K Negations.