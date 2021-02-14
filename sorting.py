array = [10, 8, 3, 5, 2, 9, 7, 1, 0, 4]


def selection_sort(array):
    max_ = None
    max_pos = None

    i = len(array)

    while i > 0:
        for n in range(i):
            if (max_ == None) or (array[n] > max_):
                max_ = array[n]
                max_pos = n
            if n == (i - 1):
                array[max_pos], array[n] = array[n], array[max_pos]
        i -= 1
        max_ = None
        max_pos = None

    return array


print(selection_sort(array))