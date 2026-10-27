class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for current in range(1, amount + 1):
            for coin in coins:
                if coin <= current:
                    dp[current] = min(
                        dp[current],
                        dp[current - coin] + 1
                    )

        return -1 if dp[amount] == amount + 1 else dp[amount]