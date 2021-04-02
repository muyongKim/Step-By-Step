# 2016년 2021/04/02
# Input
a = 5
b = 24

def solution(a,b):
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    answer = day[(sum(month[:a-1])+b) % 7]
    return answer

print(solution(a,b))