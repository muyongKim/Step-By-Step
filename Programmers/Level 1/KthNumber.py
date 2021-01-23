# K번째수
# Input
array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]

def solution(array, commands):
    answer = []

    if (100 < len(array) or len(array) == 0 
    or len(commands) == 0 or len(commands) > 50):      # 제한조건
        return print("Input is wrong") 

    for n in commands:                         # commands에서 인덱스 추출
        i = n[0]
        j = n[1]
        k = n[2]
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])        

    return answer

print(solution(array, commands))

# lambda 사용하여 풀이 가능