# 핸드폰 번호 가리기
# Input
number = "01033334444"

def solution(number):
    idx = len(number) - 4
    print(idx)
    answer = []
    
    for i in range(0,idx):
        answer.append('*')

    for j in range(idx,len(number)):
        answer.append(number[j])

    answer = "".join(answer)

    return answer

print(solution(number))