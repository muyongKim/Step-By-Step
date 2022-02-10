# 22/02/10
# Hash Table, String
# Input
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

def solution(paths):
    output = ""
    dict = {}

    for city in paths:
        dict[city[0]] = city[1]
    
    output = list(set(dict.values()) - set(dict.keys()))[0]

    return output    

print(solution(paths))