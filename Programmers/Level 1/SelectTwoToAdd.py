# 두 개 뽑아서 더하기
# Input
numbers = [5,0,2,7]

def solution(numbers):
    answer = []
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):                   # numbers[0]+numbers[1], numbers[0]+numbers[2], ...
            if numbers[i]+numbers[j] not in answer:         # 중복 제거
                answer.append(numbers[i]+numbers[j])
    return sorted(answer)

print(solution(numbers))

'''
이중 for문을 from itertools import combinations을 통해
배열의 조합을 찾을 수 있음.
하나의 for문으로 수정 가능.
'''