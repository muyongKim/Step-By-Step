# 22/02/15
# Easy
# Array, Sliding Window
# Input
nums = [-1]
k = 1

def solution(nums, k):
    max = float("-inf")

    for i in range(len(nums)-k+1):
        sub = nums[i:i+k]
        if sum(sub)/k > max:
            max = sum(sub)/k
    
    return max
#  -> Time Limit Exceeded
print(solution(nums, k))