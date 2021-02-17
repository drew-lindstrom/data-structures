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


def quicksort(array, low, high):
    if low < high:
        pivot_location = partition(array, low, high)
        quicksort(array, low, pivot_location)
        quicksort(array, pivot_location + 1, high)

    return array


def partition(array, low, high):
    pivot = array[low]
    leftwall = low

    for i in range(low + 1, high):
        if array[i] < pivot:
            array[i], array[leftwall] = array[leftwall], array[i]
            leftwall = leftwall + 1

    array[leftwall], pivot = pivot, array[leftwall]
    return leftwall


def mergsort(array):
    if n == 1:
        return array
    arrayOne = array[1 : (n / 2)]
    arrayTwo = array[(n / 2) + 1 : array[n]]
    arrayOne = mergesort(arrayOne)
    arrayTwo = mergesort(arrayTwo)

    return merge(arrayOne, arrayTwo)


def merge(a, b):
    c = []
    while a and b:
        if a[0] > b[0]:
            c.append(b[0])
            del b[0]
        else:
            c.append(a[0])
            del a[0]

    while a:
        c.append(a[0])
        del a[0]

    while b:
        c.append(b[0])
        del b[0]

    return c


print(quicksort(array, 2, 8))