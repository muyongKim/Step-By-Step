# 22/02/26
# Bit Manipulation
# Input
x = 3
y = 1

def solution(x,y):
    count = 0

    if x >= y:
        x = bin(x)[2:]
        y = bin(y)[2:].zfill(len(x))
    else:
        y = bin(y)[2:]
        x = bin(x)[2:].zfill(len(y))

    for i, j in zip(x,y):
        if i != j:
            count += 1

    return count

print(solution(x,y))
# Runtime: 47 ms, faster than 40.01% of Python3 online submissions for Hamming Distance.
# Memory Usage: 13.8 MB, less than 99.03% of Python3 online submissions for Hamming Distance.

# -> ^ 비트 연산자 사용
# def solution(x,y):
#     return bin(x^y).count("1")