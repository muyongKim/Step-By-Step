# 22/02/03
# Array, Hash Table, String
# Input
names = ["kaido","kaido(1)","kaido","kaido(1)"]

def solution(names):
    files = {}

    for i in range(len(names)):
        if names[i] in files:
            start = names[i].rfind("(")
            end = names[i].rfind(")")   
            num = names[i][start+1:end]
            new_name = names[i] + "(" + str(num) + ")"
            files[new_name] = files[names[i]] + 1
        else:
            files[names[i]] = 0


    # for i in range(len(names)):
    #     if names[i] in files:
    #         for j in range(1, i+1):
    #             new_name = names[i] + "(" + str(j) + ")"
    #             if new_name not in files:
    #                 files.append(new_name)
    #                 break
    #     else:
    #         files.append(names[i])
    
    return files

print(solution(names))