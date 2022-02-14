# 22/02/14
# Array, Hash Table
# Input
nums = [49999,100,2,100,100,4,100]

def solution(nums):
    dict = {}
    length = len(nums)
    index = []

    for n in nums:
        if n not in dict:
            dict[n] = 0
        dict[n] += 1
    
    elements = [k for k,v in dict.items() if max(dict.values()) == v]
    
    for e in elements:
        index.append([i for i,v in enumerate(nums) if v == e])
    
    for i in index:
        length = min(length, i[-1] - i[0] + 1)
    
    return length
# -> Too much runtime
#   각 숫자의 빈도수와 위치를 개별적으로 dict에 저장
    # frq = defaultdict(int) # frequency map for nums
    # fnl = {} # stores first and last index of each num
    # deg = 0  # degree
    
    # for i in range(len(nums)):
    #     frq[nums[i]] += 1
    #     deg = max(deg, frq[nums[i]])
    #     if nums[i] in fnl:
    #         fnl[nums[i]][1] = i
    #     else:
    #         fnl[nums[i]] = [i,i]
            
    # res = len(nums)
            
    # for num in frq:
    #     if frq[num] != deg:
    #         continue
    #     res = min(res, fnl[num][1] - fnl[num][0] + 1)

    # return res
print(solution(nums))