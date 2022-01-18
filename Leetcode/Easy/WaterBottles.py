# 22/01/19
# Math, Simulation
# Input
numBottles = 11
numExchange = 4

def solution(numB, numE):
    drink, empty = numB, numB

    while empty//numE >= 1:
        drink += empty // numE
        empty = empty // numE + empty % numE
    
    return drink

print(solution(numBottles, numExchange))