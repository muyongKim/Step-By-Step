# 22/02/01
# Array, Sorting
# Input
nums = [4,2,5,9,7,4,8]

def solution(nums):
    nums.sort()
    return (nums[-1]*nums[-2]) - (nums[0]*nums[1])

print(solution(nums))