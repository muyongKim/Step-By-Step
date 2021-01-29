# 모의고사 21/01/30
# Input
answers = [1,3,2,4,2]

def solution(answers):
    a = "12345"
    b = "21232425"
    c = "3311224455"

    a_cnt = 0
    b_cnt = 0
    c_cnt = 0
    dic = {'1':a_cnt,'2':b_cnt,'3':c_cnt}
    
    a = a*(len(answers)//5) + a[:len(answers)%5]
    b = b*(len(answers)//8) + b[:len(answers)%8]
    c = c*(len(answers)//10) + c[:len(answers)%10]          # 주어진 answers 길이만큼 답안 생성.
                                                            # enumerate 사용하면 각 패턴에 대한 답안을 생성할 필요없이 for문에서 %연산으로 해결 가능.
    for i in range(len(answers)):
        if answers[i] == int(a[i]):
            a_cnt += 1
        if answers[i] == int(b[i]):
            b_cnt += 1
        if answers[i] == int(c[i]):
            c_cnt += 1

    answer = sorted([int(k) for k,v in dic.items() if max(dic.values()) == v])
    
    return answer

print(solution(answers))