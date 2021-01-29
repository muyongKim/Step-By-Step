# 방 번호 2021/01/25

n = input()
n_list = [int(i) for i in n]
count = [0,0,0,0,0,0,0,0,0]     # 0 ~ 8의 개수 count
                                # 6, 9는 같은 숫자 취급

for j in n_list:
    idx = j
    if idx == 9:
        idx = 6
    count[idx] += 1
count[6] = (count[6]+1)//2      # 666 -> 1.5 -> 2세트
                                # 66666 -> 2.5 -> 3세트
print(max(count))