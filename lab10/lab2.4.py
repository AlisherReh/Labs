
def knapsack(weights, values, max_weight):
    n = len(weights)
    dp = [[0 for j in range(max_weight + 1)] for i in range(n + 1)]

    for i, (weight, value) in enumerate(zip(weights, values), start=1):
        for j in range(1, max_weight + 1):
            if weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

    return dp[n][max_weight]


weights = [10, 20, 30]
values = [60, 100, 120]
max_weight = 50
    
max_value = knapsack(weights, values, max_weight)
print(max_value)
