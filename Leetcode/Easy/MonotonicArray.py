# 22/02/09
# Array
# Input
nums = [1,2,3]

def solution(nums):
    tmp = nums[0]

    if nums[0] <= nums[-1]:
        for n in nums[1:]:
            if n < tmp:
                return False
            tmp = n
    else:
        for n in nums[1:]:
            if n > tmp:
                return False
            tmp = n

    return True

print(solution(nums))