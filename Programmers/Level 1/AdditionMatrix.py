# 행렬의 덧셈 2021/01/31
# Input
arr1 = [[1],[2]]
arr2 = [[3],[4]]

def solution(arr1,arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for num1,num2 in zip(arr1[i],arr2[i]):
            answer[i].append(num1+num2)
    return answer

print(solution(arr1,arr2))