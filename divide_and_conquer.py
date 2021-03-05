def euclidean_algorithm(x, y):
    if x == 0:
        return y
    return euclidean_algorithm(y % x, x)