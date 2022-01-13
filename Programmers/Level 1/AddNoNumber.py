# 없는 숫자 더하기 2022/01/13
# Input
nums = [1,2,3,4,6,7,8,0]

def solution(nums):
    sum = 45

    for n in nums:
        sum -= n
    
    return sum

print(solution(nums))