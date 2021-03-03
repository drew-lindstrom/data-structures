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


def find_sum(lst, n):
    dictionary = {}
    lst.sort()

    for i in range(len(lst)):
        dictionary[lst[i]] = n - lst[i]

    for i in range(len(lst)):
        if dictionary[lst[i]] in lst:
            return [lst[i], dictionary[lst[i]]]


def pivoted_binary_search(lst, n, key):

    counter = 0
    low = 0
    high = len(lst) - 1
    mid = 0
    temp = 0

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            counter += 1
            break
        else:
            counter += 1

    temp = counter

    while temp > 0:
        lst.append(lst[0])
        lst.pop(0)
        temp -= 1

    while low <= high:
        mid = (high + low) // 2

        if lst[mid] < key:
            low = mid + 1

        elif lst[mid] > key:
            high = mid - 1

        else:
            break

    print(low)
    print(counter)
    return high + counter - 1


def anagrams(lst):
    dictionary = {}

    for string in lst:
        key = "".join(sorted(string))
        if key in dictionary.keys():
            dictionary[key].append(string)
        else:
            dictionary[key] = []
            dictionary[key].append(string)

    result = []
    for key, value in dictionary.items():
        if len(value) >= 2:
            result.append(value)

    result = sorted(result)

    return result


def sort_binary_list(lst):
    size = len(lst)

    for i in range(size):
        for j in range(0, size - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


def search_insert_position(lst, value):
    size = len(lst)

    if size < 1:
        return -1

    start = 0
    end = size - 1

    pos = 0

    while start <= end:
        mid = start + (end - start) // 2

        if lst[mid] == value:
            return mid
        elif lst[mid] > value:
            end = mid - 1
            pos = mid
        else:
            start = mid + 1
            pos = mid + 1

    return pos


print(pivoted_binary_search([7, 8, 9, 0, 3, 5, 6], 0, 3))