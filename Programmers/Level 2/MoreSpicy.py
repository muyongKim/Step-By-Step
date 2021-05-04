# 더 맵게 2021/05/05
# Input
scoville = [1,2,3,9,10,12]
k = 7

from heapq import heappop, heappush, heapify

def solution(scoville, k):
    heapify(scoville)
    cnt = 0

    while scoville[0] < k:
        if len(scoville) == 1:
            return -1
        
        heappush(scoville, heappop(scoville) + heappop(scoville)*2)
        cnt += 1
    
    return cnt

print(solution(scoville,k))