# 체육복 2021/03/28
# Input
n = 5
lost = [2,4]
reserve = [3]

def solution(n, lost, reserve):
    answer = 0
    available = [1 for i in range(n)]

    for i in lost:
        available[i-1] = 0
    
    for i in reserve:
        if available[i-1] == 0:
            reserve.remove(i)
            available[i-1] += 1
    
    print(available)
    print(reserve)
    
    for i in range(len(available)):
        # 첫번째 값 처리
        if i == 0 and available[i] == 1 and available[i+1] == 0 and reserve.count(i+1) == 1:
            available[i+1] += 1
            reserve.remove(i+1)
        elif available[i] == 1 and reserve.count(i+1) == 1 and (available[i-1:i] == 0 or available[i+1:i+2] == 0):
            if available[i-1] == 0:
                available[i-1] += 1
                reserve.remove(i+1)
            else:
                available[i+1] += 1
                reserve.remove(i+1)
        
        if available.count(0) == 0:
            break
    
    answer = available.count(1)

    return answer
    
print(solution(n, lost, reserve))