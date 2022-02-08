# 22/02/08
# Array, Queue, Simulation
# Input
tickets = [5,1,1,1]
k = 0

def solution(tickets, k):
    time = 0

    while True:
        for i in range(len(tickets)):
            if tickets[i] == 0:
                continue
            else:
                tickets[i] -= 1
                time += 1
            if tickets[k] == 0:
                return time

print(solution(tickets, k))        