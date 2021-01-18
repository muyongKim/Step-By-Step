'''
정수 배열 numbers가 주어집니다. 
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 
만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
'''
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