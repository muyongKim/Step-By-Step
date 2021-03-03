# 행렬의 곱셈 2021/03/03
# Input
arr1 = [[1,4],[3,2],[4,1]]
arr2 = [[3,3],[3,3]]

def solution(arr1, arr2):
    answer = [[0 for col in range(len(arr2[0]))] for row in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer

print(solution(arr1,arr2))