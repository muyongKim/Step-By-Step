# 22/02/17 최소직사각형
# Input
sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

def solution(sizes):
    for size in sizes:
        size.sort()
    width = max(list(map(lambda x:x[1],sizes)))
    height = max(list(map(lambda x:x[0],sizes)))
    
    return width*height

print(solution(sizes))