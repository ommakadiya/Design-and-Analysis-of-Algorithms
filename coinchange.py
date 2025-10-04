def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]

# Example usage:
coins = [1, 5, 6, 8]
amount = 11
print("Minimum number of coins is", coin_change(coins, amount))