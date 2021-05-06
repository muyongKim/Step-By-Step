# 가장 큰 수
# Input
numbers = [6,2,10]

import functools

def compare(a, b):
    if int(a+b) > int(b+a):         # a+b > b+a 이면 자리를 바꾸지 않음
        return -1
    elif int(a+b) < int (b+a):      # a+b < b+a 이면 자리를 바꿈
        return 1
    else : return 0                 # a+b == b+a

def solution(numbers):
    answer=''

    if len(numbers) > 100000:           # 제한조건
        print("Array is too big")
        return
    
    tmp = [str(n) for n in numbers]     # number의 수를 str로 바꾸어 배열에 저장
    tmp = sorted(tmp, key=functools.cmp_to_key(compare))

    if tmp[0]=='0':                     # numbers = [0, 0, 0]의 경우 '0'으로 return
        return '0'

    for num in tmp:
        answer += num
    
    return answer

print(solution(numbers))