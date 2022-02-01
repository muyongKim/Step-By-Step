# 22/02/01
# Array, Hash Table, Counting
# Input
arr = [1,2,2,3,3,3]

def solution(arr):
    arr.sort(reverse=True)
    
    for i in arr:
        if arr.count(i) == i:
            return i
    return -1

print(solution(arr))