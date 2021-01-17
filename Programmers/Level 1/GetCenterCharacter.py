'''
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
'''

# Input
s = 'abcde'

def solution(s):
    answer = ''
    idx = int(len(s)/2)
    if (len(s) % 2 == 0):
        answer = s[(idx -1)] + s[idx]
    else:
        answer = s[idx]
    return answer

print(solution(s))

# if문 없이 문자열 슬라이싱을 통해 구현 가능