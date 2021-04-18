# 다리를 지나는 트럭 2021/04/14
# Input
length = 2
weight = 10
truck = [7,4,5,6]

from collections import deque

def solution(length, weight, truck):
    crossed = []
    crossing = []
    time = 0
    weight_t = 0
    deq_t = deque(truck)
    deq_c = deque(crossing)

    deq_c.append([deq_t.popleft(),0])
    weight_t += deq_c[0][0]
    deq_c[0][1] += 1
    time += 1

    while deq_c:
        if deq_t and weight_t + deq_t[0] <= weight:
            deq_c.append([deq_t.popleft(),0])
            weight_t += deq_c[0][0]
            
            for t in deq_c:
                t[1] += 1
            time += 1
        else:
            for t in deq_c:
                t[1] += 1
            time += 1
    
        if deq_c and deq_c[0][1] > length:
            weight_t -= deq_c[0][0]
            crossed.append(deq_c.popleft())

            if deq_t and weight_t + deq_t[0] <= weight:
                deq_c.append([deq_t.popleft(),0])
                weight_t += deq_c[0][0]

                for t in deq_c:
                    t[1] += 1
                time += 1

    return time

print(solution(length,weight,truck))