# 자연수 뒤집어 배열로 만들기
# Input
n = 12345

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

print(solution(n))