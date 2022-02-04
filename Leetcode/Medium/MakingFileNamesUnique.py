# 22/02/03
# 22/02/04 solved
# Array, Hash Table, String
# Input
names = ["a", "a(3)", "a", "a", "a"]

# def solution(names):
    # files = []
    # 
    # for i in range(len(names)):
    #     if names[i] in files:
    #         for j in range(1, i+1):
    #             new_name = names[i] + "(" + str(j) + ")"
    #             if new_name not in files:
    #                 files.append(new_name)
    #                 break
    #     else:
    #         files.append(names[i])
    #
    # return files
    # 시간 제한 초과

def solution(names):
    files = {}
    output = []

    for name in names:
        if name not in files:
            output.append(name)
            files[name] = 1
        else:
            k = files[name]
            
            while name + f"({k})" in files:
                k += 1
            new_name = name + f"({k})"
            output.append(new_name)
            files[name] += 1
            files[new_name] = 1
    
    return output

print(solution(names))