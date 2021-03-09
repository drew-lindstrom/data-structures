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