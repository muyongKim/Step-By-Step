# 비밀지도 2018 kakao blind recruitment 
# Input
n = 5
arr1, arr2 = [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]

def solution(n, arr1, arr2):
    answer = []
    maps = []

    for i in range(n):
        maps.append(str(bin(arr1[i] | arr2[i]))[2:])
        if not len(maps[i]) == n:
            maps[i] = ' ' + maps[i]
    
    for m in maps:
        tmp = ''
        for i in range(n):
            if m[i] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer

print(solution(n,arr1,arr2))        