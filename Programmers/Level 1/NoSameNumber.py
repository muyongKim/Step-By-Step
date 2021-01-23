# 같은 숫자는 싫어
# Input
arr = [1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    for i in arr:
        index = 0
        if i not in answer:             # answer 배열에 없는 값 추가
            answer.append(i)
        else :
            if i != answer[index-1]:    # 이미 answer 배열에 존재하지만 연속되지 않는 값 추가
                answer.append(i)
        index += 1
    return answer
    
print(solution(arr))