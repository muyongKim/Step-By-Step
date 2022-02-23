# 22/02/23
# Array, Simulation
# Input
nums = [5,0,1,2,3,4]

def solution(nums):
    output = [0]*len(nums)

    for i in range(len(nums)):
        output[i] = nums[nums[i]]
    
    return output

print(solution(nums))
# Runtime: 218 ms, faster than 19.42% of Python3 online submissions for Build Array from Permutation.
# Memory Usage: 14.2 MB, less than 77.89% of Python3 online submissions for Build Array from Permutation.