def solution(s):
    char_list = ""
    index = 0
    for i in s:
        if i.isalpha():
            index += 1
            if index % 2 != 0:
                char_list += i.upper()
            else :
                char_list += i.lower()
        else:
            index = 0
            char_list += ' '
            continue

    return char_list

print(solution("try hello world"))