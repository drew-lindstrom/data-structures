import math


def find_largest_number(number_of_digits, sum_of_digits):

    answer = []

    while sum_of_digits > 0 or number_of_digits > 0:
        if number_of_digits < 0:
            return [-1]

        if sum_of_digits == 0:
            answer.append(0)
        else:
            num = 9
            while sum_of_digits - num < 0:
                num -= 1
            answer.append(num)
            sum_of_digits = sum_of_digits - num

        number_of_digits -= 1

    return answer


def egyptian_fraction(numerator, denominator):
    lst_denominator = []

    while numerator != 0:
        x = math.ceil(denominator / numerator)

        lst_denominator.append(x)

        numerator = x * numerator - denominator
        denominator = denominator * x

    return lst_denominator


# print(find_largest_number(2, 9))
print(egyptian_fraction(2, 3))