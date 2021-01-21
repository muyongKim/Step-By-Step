'''

'''

number = 9876
k = 2

def solution(number,k):
    answer = ''
    tmp = [int(n) for n in str(number)]
    remove = []
    cnt = 0
    i = 0
    idx = 0

    while cnt < k:
        if tmp[i] > tmp[i+1]:
            remove.append(i+1)
            cnt += 1
            i += 1
            print(remove)
        elif tmp[i] < tmp[i+1]:
            remove.append(i)
            cnt += 1
            i += 1
            print(remove)
        else: 
            i += 1
            print(remove)
    
    print(tmp)
    for n in range(0,len(remove)):
        tmp.pop(remove[n]-idx)
        idx += 1
    print(tmp)
    answer = "".join(map(str,tmp))
  
    return answer

print(solution(number,k))