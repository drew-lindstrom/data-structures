array = [10, 8, 3, 5, 2, 9, 7, 1, 0, 4]


def selection_sort(array):
    i = len(array)

    while i > 0:
        max_ = None
        max_pos = None
        for n in range(i):
            if (max_ == None) or (array[n] > max_):
                max_ = array[n]
                max_pos = n
            if n == (i - 1):
                array[max_pos], array[n] = array[n], array[max_pos]
        i -= 1

    return array


def insertion_sort(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j = j - 1

    return array


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


print(bubble_sort(array))