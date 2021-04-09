# 주식가격 2021/04/09
# Input
prices = [1,2,3,2,3]

def solution(prices):
    answer = []

    for i in range(len(prices)):
        time = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                time += 1
            else:
                time += 1
                break
        answer.append(time)
    return answer

print(solution(prices))