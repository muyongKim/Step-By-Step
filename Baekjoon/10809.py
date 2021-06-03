# 알파벳 찾기 2021/06/03
# 분류 : 구현, 문자열

s = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
loc = []

for a in alphabet:
    loc.append(str(s.find(a)))

print(" ".join(loc))