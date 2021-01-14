def solution (n):
    answer = []
    index = len(str(n))

    if index > 10 :
        return print("number is too big")
    else :
        for i in range(index):
            answer.append(n % 10)
            n = int(n/10)
    return answer

print(solution(12345))