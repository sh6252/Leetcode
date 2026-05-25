class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True

        window = 0  # number of reachable indices in range

        for i in range(1, n):
            # add new index into window
            if i - minJump >= 0 and dp[i - minJump]:
                window += 1

            # remove old index from window
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                window -= 1

            dp[i] = (window > 0 and s[i] == '0')

        return dp[-1]