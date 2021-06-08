# 다리를 지나는 트럭 2021/04/14
# Input
length = 2
weight = 10
truck = [7,4,5,6]

from collections import deque

def solution(length, weight, truck):
    truck.reverse()
    queue_t = deque()
    queue_c = deque()
    time = 0

    while truck or queue_c:
        if queue_t:
            if queue_t[0] == length:
                queue_c.popleft()
                queue_t.popleft()
        if truck:
            if sum(queue_c) + truck[-1] <= weight:
                queue_c.append(truck.pop())
                queue_t.append(0)
        for i in range(len(queue_t)):
            queue_t[i] += 1
        time += 1

    return time

print(solution(length,weight,truck))