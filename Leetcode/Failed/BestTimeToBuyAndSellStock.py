# 22/02/15
# Easy
# Array, Dynamic Programming
# Input
prices = [7,6,4,3,1]

def solution(prices):
    profit = 0

    for i in range(len(prices)):
        sub = prices[i:]
        for j in range(1,len(sub)):
            if prices[i] == max(sub):
                break
            elif (sub[j] - prices[i]) > profit:
                profit = sub[j] - prices[i]
    
    return profit
# -> Time Limit Exceeded
print(solution(prices))