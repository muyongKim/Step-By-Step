# 문자열을 정수로 바꾸기
# input
s = '-1234'

def solution(s):
    answer = int(s)
    return answer

print(solution(s))

# Too simple...
# 부호가 있는 숫자 문자열을 int로 변환해도 +,- 부호를 인식