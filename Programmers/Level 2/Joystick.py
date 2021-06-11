# 조이스틱 2021/06/11
# Input
name = 'JEROEN'

def solution(name):
    cnt = 0

    for n in name:
        if ord(n) <= 78:
            cnt += ord(n) - 65
        else:
            cnt += 91 - ord(n)
    
    flag = False
    for i in range(len(name)):
        if flag and name[i] != 'A':
            left = i
            break
        elif name[i] != 'A':
            flag = True
    
    for j in reversed(range(len(name))):
        if name[j] != 'A':
            right = j
            break
    
    if name[1:right+1].count('A') < name[left:].count('A'):
        cnt += len(name[:right+1]) - 1
    else:
        cnt += len(name[left:])
    
    return cnt
print(solution(name))