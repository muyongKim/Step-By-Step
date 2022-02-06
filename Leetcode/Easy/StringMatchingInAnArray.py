# 22/02/06
# String, String Matching
# Input
words = ["mass","as","hero","superhero"]

def solution(words):
    output = []

    for word in words:
        for other in words:
            if word in other and word != other and word not in output:
                output.append(word)
    
    return output

print(solution(words))