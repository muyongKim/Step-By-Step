# 폰켓몬 2021/03/10
# Input
nums = [3,1,2,3]

def solution(nums):
    kind = list(set(nums))
    pick = int(len(nums) / 2)
    
    if len(kind) > pick:
        return pick
    else:
        return len(kind)

print(solution(nums))