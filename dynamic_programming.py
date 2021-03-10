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


print(find_min_fee([1, 2, 5, 2]))