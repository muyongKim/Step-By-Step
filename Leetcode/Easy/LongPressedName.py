# 22/02/06
# Two Pointers, String
# Input
name = "saeed"
typed = "ssaedd"

def solution(name, typed):
    cur = 0

    for i in range(len(name)):
        cnt = 0
        if i != len(name)-1 and name[i] == name[i-1]:
            continue
        for j in range(cur, len(typed)):
            if name[i] != typed[j]:
                cur = j
                break
            else:
                cnt += 1
        if cnt == 0:
            return False
    return True

print(solution(name,typed))