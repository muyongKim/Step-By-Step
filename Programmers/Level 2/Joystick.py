# 조이스틱 2021/06/11
# Input
name = 'ABAAAABB'

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
        flag = True
    
    for j in reversed(range(len(name))):
        if name[j] != 'A':
            right = j
            break
    
    idx = 0
    not_a = len(name) - name.count('A')
    passed = []
    while len(passed) != not_a:
        if name[idx] != 'A':
            passed.append(name[idx])
            for k in range(idx+1,len(name)):
                if name[k] != 'A':
                    left = name[k]
        if name[idx+1:right+1].count('A') <= name[left:].count('A'):
            idx += 1
        else:
            idx -= 1
        cnt += 1

    return cnt
print(solution(name))