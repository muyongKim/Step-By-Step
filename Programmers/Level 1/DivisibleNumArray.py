# 나누어 떨어지는 숫자 배열
# Input
arr = [3,2,6]
divisor = 10

def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    answer.sort()

    if len(answer) == 0:
        answer.append(-1)
    return answer

print(solution(arr,divisor))