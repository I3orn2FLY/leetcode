def coinChange(coins, amount: int) -> int:
    MC = {0: 0}

    for v in range(1, amount + 1):
        min_val = None

        for coin in coins:
            left_over = v - coin
            if left_over < 0:
                continue

            mc = MC[left_over]

            if mc == -1:
                continue

            if min_val is None:
                min_val = 1 + mc

            if min_val > 1 + mc:
                min_val = 1 + mc

        if min_val is None:
            MC[v] = -1
        else:
            MC[v] = min_val

    return MC[amount]


coinChange([1, 2, 5], amount = 11)