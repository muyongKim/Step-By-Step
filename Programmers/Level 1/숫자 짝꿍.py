# 22.10.13
# input
X = "12321"
Y = "42531"


def solution(X, Y):
    friend = []

    if not (set(X) & set(Y)):
        return "-1"
    elif set(X) & set(Y) == {'0'}:
        return "0"

    for n in list(set(X) & set(Y)):
        friend += [n] * min(X.count(n), Y.count(n))
    friend.sort(reverse=True)

    return "".join(friend)

print(solution(X, Y))