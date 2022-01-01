# 부족한 금액 계산하기  2022/01/01
# Input
price, money, count = 3, 20, 4

def solution(price, money, count):
    amount = 0

    for i in range(1, count+1):
        amount += price * i
    
    if amount > money:
        return amount - money
    else:
        return 0

print(solution(price, money, count))
