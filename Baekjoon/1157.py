# 단어 공부 2021/06/04
# 분류 : 구현, 문자열

word = input()

alphabet = {}
word = word.upper()
for w in word:
    if w not in alphabet:
        alphabet[w] = 0

for k in alphabet:
    alphabet[k] = word.count(k)

most = [k for k,v in alphabet.items() if max(alphabet.values()) == v]

if len(most) >= 2:
    print('?')
else:
    print(most[0])