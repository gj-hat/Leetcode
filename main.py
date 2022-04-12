class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def fib1(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib1(n - 1) + self.fib1(n - 2)


if __name__ == "__main__":
    a = Solution()
    print("fib:", a.fib(45))
    print("fib1:", a.fib1(45))
