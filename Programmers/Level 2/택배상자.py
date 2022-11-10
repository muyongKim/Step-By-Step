# 22.11.11
# https://school.programmers.co.kr/learn/courses/30/lessons/131704
# input
order = [5, 4, 3, 2, 1]


def solution(order):
    answer = 0
    stack = []
    boxes = [x for x in range(1, len(order) + 1)][::-1]

    for o in order:
        if boxes:
            while (True):
                if not boxes:
                    break

                box = boxes.pop()

                if box != o:
                    if stack and stack[-1] == o:
                        answer += 1
                        stack.pop()
                        boxes.append(box)
                        break
                    else:
                        stack.append(box)
                else:
                    answer += 1
                    break

        elif stack[-1] == o:
            answer += 1
            stack.pop()
        else:
            break

    return answer


print(solution(order))