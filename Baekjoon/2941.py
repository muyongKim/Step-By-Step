# 크로아티아 알파벳 2021/06/03
# 분류 : 구현, 문자열

word = input()

c_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for c in c_alphabet:
    if c in word:
        word = word.replace(c,'1')

print(len(word))