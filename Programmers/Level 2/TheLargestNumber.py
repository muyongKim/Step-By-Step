'''
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 
이 중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

예) [6,10,2] -> 6210
'''

# sorted, compare 함수 활용이 핵심

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

numbers = [6,2,10]
print(solution(numbers))