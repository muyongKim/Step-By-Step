'''
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 
테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 
카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
'''
# # Input
brown = 24
yellow = 24

def solution(brown,yellow):
    divisor = []

    for i in range(1, yellow+1):            # yellow의 약수
        if yellow % i == 0:                 # but 실행시간이 길어짐
            divisor.append(i)
    
    divisor.reverse()

    for n in range(0, int(len(divisor)/2)+1):
        if brown == 2*divisor[n] + 2*(yellow/divisor[n]+2):
            answer = [divisor[n]+2, int(yellow/divisor[n])+2]
            return answer

print(solution(brown,yellow))