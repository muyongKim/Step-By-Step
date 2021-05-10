# 로또의 최고 순위와 최저 순위 2021/05/10
# Input
lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
    match = 0

    for num in lottos:
        if num != 0 and num in win_nums:
            match += 1
    
    if match + lottos.count(0) >= 2:
        highest = 7 -(match + lottos.count(0))
    else:
        highest = 6

    return [highest,match]

print(solution(lottos,win_nums))