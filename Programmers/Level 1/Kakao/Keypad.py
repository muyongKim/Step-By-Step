# 키패드 누르기 2020 kakao internship 2021/04/05
# Retry
# Input
numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

def solution(numbers, hand):
    answer = ""
    keypad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    left_x, left_y = 0, 3
    right_x, right_y = 2, 3
    left, right = [],[]

    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            left.append(numbers[i])
            answer += "L"
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            right.append(numbers[i])
            answer += "R"
        elif numbers[i] == 2 or numbers[i] == 5 or numbers[i] == 8 or numbers[i] == 0:
            if numbers[i] == 0:
                x, y = 1,3
            else:
                x = numbers[i] % 3 - 1
                if x == -1:
                    x = 2

                y = numbers[i] // 3
                if numbers[i] % 3 == 0:
                    y -= 1

            if len(left) > 0:
                if left[-1] == 0:
                    left_x, left_y = 1, 3
                else:
                    left_x = left[-1] % 3 - 1
                    if left_x == -1:
                        left_x = 2
                    left_y = left[-1] // 3
                    if left[-1] % 3 == 0:
                        left_y -= 1

            if len(right) > 0:
                if right[-1] == 0:
                    right_x, right_y = 1, 3
                else:
                    right_x = right[-1] % 3 - 1
                    if right_x == -1:
                        right_x = 2
                    right_y = right[-1] // 3
                    if right[-1] % 3 == 0:
                        right_y -= 1
            
            left_l = abs(x-left_x) + abs(y-left_y)
            right_l = abs(x-right_x) + abs(y-right_y)

            if left_l > right_l:
                right.append(numbers[i])
                answer += "R"
            elif left_l < right_l:
                left.append(numbers[i])
                answer += "L"
            else:
                if hand == "right":
                    right.append(numbers[i])
                    answer += "R"
                else:
                    left.append(numbers[i])
                    answer += "L"
    return answer

print(solution(numbers, hand))