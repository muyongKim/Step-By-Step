# 통계학 2021/06/08
# 분류 : 구현, 정렬
import sys
from collections import Counter

N = int(sys.stdin.readline())
num = []
for i in range(N):
    num.append(int(sys.stdin.readline()))
num.sort()

print(round(sum(num)/N))
print(num[(N//2)])

k = Counter(num).most_common()
if N == 1:
    print(num[0])
else:
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:
        print(k[0][0])

print(max(num) - min(num))