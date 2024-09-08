def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    dp = [float("inf")] * (target + 1)  # To store minimum coins needed for each amount
    dp[0] = 0  # No coins needed to make 0

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[target] == float("inf"):
        raise ValueError("can't make target with given coins")

    result = []
    while target > 0:
        for coin in coins:
            if target >= coin and dp[target - coin] == dp[target] - 1:
                result.append(coin)
                target -= coin
                break

    return result
