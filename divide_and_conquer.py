def euclidean_algorithm(x, y):
    if x == 0:
        return y
    return euclidean_algorithm(y % x, x)


def find_peak(lst):
    if len(lst) is 0:
        return -1

    if len(lst) is 1:
        return lst[0]

    for i in range(1, len(lst) - 1):
        if lst[i] >= lst[i - 1] and lst[i] >= lst[i + 1]:
            return lst[i]

    if lst[0] >= lst[1]:
        return lst[0]
    elif lst[len(lst) - 1] >= lst[len(lst) - 2]:
        return lst[len(lst) - 1]

    return -1