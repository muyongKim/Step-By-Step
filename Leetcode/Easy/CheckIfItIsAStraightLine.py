# 22/02/07
# Array, Math, Geometry
# Input
coordinates = [[1,2],[2,3]]

def solution(coord):
    def getSlope(i):
        dx = coord[i+1][0] - coord[i][0]
        if dx != 0:
            return (coord[i+1][1] - coord[i][1]) / (coord[i+1][0] - coord[i][0])
        else:
            return float("inf")
    
    slope = getSlope(0)
    for i in range(1, len(coord)-1):
        if getSlope(i) != slope:
            return False
    return True

print(solution(coordinates))