def count_min_jumps(jumps):
    n = len(jumps)
    dp = [math.inf for _ in range(n)]
    dp[0] = 0

    for start in range(n - 1):
        end = start + 1
        while end <= start + jumps[start] and end < n:
            dp[end] = min(dp[end], dp[start] + 1)
            end += 1

    return dp[n - 1]


def find_min_fee(fee):
    return find_min_fee_recursive(fee, 0)


def find_min_fee_recursive(fee, step):
    if step > len(fee) - 1:
        return 0

    take_1_step = find_min_fee_recursive(fee, step + 1)
    take_2_step = find_min_fee_recursive(fee, step + 2)
    take_3_step = find_min_fee_recursive(fee, step + 3)

    _min = min(take_1_step, take_2_step, take_3_step)

    return _min + fee[step]


def find_min_fee_dynamic(fee):
    dp = [-1] * len(fee)
    return find_min_fee_recursive(fee, 0, dp)


def find_min_fee_dynamic_util(fee, step, dp):
    if step > len(fee) - 1:
        return 0

    take_1_step = find_min_fee_dynamic_util(fee, step + 1, dp)
    take_2_step = find_min_fee_dynamic_util(fee, step + 2, dp)
    take_3_step = find_min_fee_dynamic_util(fee, step + 3, dp)

    dp[step] = fee[step] + min(take_1_step, take_2_step, take_3_step)

    return dp[step]


def find_min_fee_tabulation(fee):
    n = len(fee)
    dp = [0 for x in range(n + 1)]
    dp[0] = 0
    dp[1] = fee[0]
    dp[2] = fee[0]

    for i in range(2, n):
        dp[i + 1] = min(fee[i] + dp[i], fee[i - 1] + dp[i - 1], fee[i - 2] + dp[i - 2])

    return dp[n]


def find_lps_length(string):
    n = len(string)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_lps_length_dynamic(string, 0, len(string) - 1, dp)


def find_lps_length_recursive(string, pointer1, pointer2):

    if pointer1 > pointer2:
        return 0

    if pointer1 == pointer2:
        return 1

    if string[pointer1] == string[pointer2]:
        return 2 + find_lps_length_recursive(string, pointer1 + 1, pointer2 - 1)

    c1 = find_lps_length_recursive(string, pointer1 + 1, pointer2)
    c2 = find_lps_length_recursive(string, pointer1, pointer2 - 1)
    return max(c1, c2)


def find_lps_length_dynamic(string, pointer1, pointer2, dp):

    if pointer1 > pointer2:
        return 0

    if pointer1 == pointer2:
        return 1

    if dp[pointer1][pointer2] == -1:
        if string[pointer1] == string[pointer2]:
            dp[pointer1][pointer2] = 2 + find_lps_length_recursive(
                string, pointer1 + 1, pointer2 - 1
            )
        else:
            c1 = find_lps_length_recursive(string, pointer1 + 1, pointer2)
            c2 = find_lps_length_recursive(string, pointer1, pointer2 - 1)
            dp[pointer1][pointer2] = max(c1, c2)

    return dp[pointer1][pointer2]


def find_lps_length_tabulation(string):
    n = len(string)
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            if string[startIndex] == string[endIndex]:
                dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
            else:
                dp[startIndex][endIndex] = max(
                    dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1]
                )

    return dp[0][n - 1]


def find_LPS_length(st):
    return find_LPS_length_recursive(st, 0, len(st) - 1)


def find_LPS_length_recursive(st, startIndex, endIndex):
    if startIndex > endIndex:
        return 0

    if startIndex == endIndex:
        return 1

    if st[startIndex] == st[endIndex]:
        remainingLength = endIndex - startIndex - 1
        if remainingLength == find_LPS_length_recursive(
            st, startIndex + 1, endIndex - 1
        ):
            return remainingLength + 2
        # else:
        #     return

    c1 = find_LPS_length_recursive(st, startIndex + 1, endIndex)
    c2 = find_LPS_length_recursive(st, startIndex, endIndex - 1)
    return max(c1, c2)


print(find_LPS_length("abdbca"))