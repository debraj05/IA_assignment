import sys
def no_ways_toattend(n):
    """
        Return the result of
        The number of ways to attend classes over N days/The probability that you will miss your graduation ceremony.
    """
    dp = [[0] * 4 for _ in range(n + 1)]

    dp[0][0] = 1
    for i in range(1, n + 1):
        # attended on day i
        dp[i][0] = sum(dp[i - 1][:4])
        for j in range(1, 4):
            dp[i][j] = dp[i - 1][j - 1]

    return str(sum(dp[n][1:])) + '/' + str(sum(dp[n]))

days = int(sys.argv[1])
print(no_ways_toattend(days))
