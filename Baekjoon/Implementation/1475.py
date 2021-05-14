# 방 번호 2021/01/25

n = input()
n_list = [int(i) for i in n]
count = [0,0,0,0,0,0,0,0,0]     

for j in n_list:
    idx = j
    if idx == 9:
        idx = 6
    count[idx] += 1
count[6] = (count[6]+1)//2      
print(max(count))