# 키패드 누르기 2020 kakao internship 2021/04/05
# Retry
# Input
numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

def distance(hand, m):
    dist = abs(hand[0] - m[0]) + abs(hand[1] - m[1])
    return dist

def solution(numbers, hand):
    answer = ""
    left, right, middle = [0,3], [2,3], [1,0]

    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            left[0] = 0
            left[1] = (n-1) // 3
            answer += "L"
        elif n == 3 or n == 6 or n == 9:
            right[0] = 2
            right[1] = (n-1) // 3
            answer += "R"
        elif n == 2 or n == 5 or n == 8 or n == 0:
            if n == 0:
                middle[1] = 3
            else:
                middle[1] = (n-1) // 3
            distL, distR = distance(left, middle), distance(right, middle)
            
            if distL > distR: 
                right[0], right[1] = middle[0], middle[1]
                answer += "R"
            elif distL < distR:
                left[0], left[1] = middle[0], middle[1]
                answer += "L"
            else:
                if hand == "right":
                    right[0], right[1] = middle[0], middle[1]
                    answer += "R"
                else:
                    left[0], left[1] = middle[0], middle[1]
                    answer += "L"
    return answer

print(solution(numbers, hand))