# 그룹 단어 체커

n = int(input())
group = n

for i in range(0,n):
    word = list(input())
    
    for j in range(0,len(word)-1):
        char = word[j]              # 현재 알파벳
        tmp = word[j+1:]
        str_tmp = "".join(tmp)      # 뒷 문자열

        if char != word[j+1]:               # 다음 알파벳이 현재 알파벳과 다를 때
            if str_tmp.find(char) != -1:    # 뒷 문자열에서 현재 알파벳이 존재할 경우
                group -= 1                  # 그룹 단어 X
                break
print(group)