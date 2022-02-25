# 22/02/25
# Input
nums = [1,3,5,4,2,3,4,5]

def solution(nums):
    output = []
    length = 1

    for i in range(1,len(nums)):
        if nums[i-1] >= nums[i]:
            output.append(length)
            length = 1
        else:
            length += 1
    output.append(length)

    return max(output)

print(solution(nums))
# Runtime: 111 ms, faster than 47.55% of Python3 online submissions for Longest Continuous Increasing Subsequence.
# Memory Usage: 15.2 MB, less than 97.99% of Python3 online submissions for Longest Continuous Increasing Subsequence.
