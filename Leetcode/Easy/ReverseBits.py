# 22/02/11
# Divide and Conquer, Bit Manipulation
# Input
n = "00000010100101000001111010011100"

def solution(n):
    n = str(format(n, '032b'))[::-1]
    return int(n, 2)

print(solution)
