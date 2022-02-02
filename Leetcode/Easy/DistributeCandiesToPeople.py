# 22/02/02
# Math, Simulation
# Input
candies = 12
num_people = 4

def solution(c, n):
    arr = [0 for x in range(n)]
    sum, start = 0, 1

    while True:
        for i in range(n):
            if c - sum < start + i:
                arr[i] += c-sum
                return arr
            else:
                arr[i] += start+i
                sum += start+i
        start += n

print(solution(candies, num_people))