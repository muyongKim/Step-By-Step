'''
문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

제한 조건
s의 길이는 1 이상 5이하입니다.
s의 맨앞에는 부호(+, -)가 올 수 있습니다.
s는 부호와 숫자로만 이루어져있습니다.
s는 0으로 시작하지 않습니다.
'''

# input
s = '-1234'

def solution(s):
    answer = int(s)
    return answer

print(solution(s))

# Too simple...
# 부호가 있는 숫자 문자열을 int로 변환해도 +,- 부호를 인식