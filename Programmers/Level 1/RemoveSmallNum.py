# 제일 작은 수 제거하기
# Input
arr = [4,3,2,1]

def solution(arr):
    answer = []
    arr.remove(min(arr))
    answer = arr
    
    if len(answer) == 0:
        answer = [-1]

    return answer

print(solution(arr))