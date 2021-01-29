# OX퀴즈 21/01/24

n = int(input())
sum_list = []

for i in range(0,n):
    score = 0
    sum = 0
    answer = list(input())
    
    for j in answer:
        if j == 'O':
            score += 1
            sum += score
        else:
            score = 0
    sum_list.append(sum)

for j in sum_list:
    print(j)