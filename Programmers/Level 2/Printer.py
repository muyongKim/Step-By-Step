# 프린터 2021/04/08
# Input
p = [1,2,3,4]
location = 0

def solution(p,location):
    cnt = 0

    while p:
        front = p.pop(0)

        if not p:
            cnt += 1
            return cnt

        if front < max(p):
            p.append(front)
            if location == 0:
                location = len(p)-1
                continue
            location -= 1
            continue
        cnt += 1
        
        if location == 0:
            return cnt
        location -= 1

print(solution(p,location))