class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math
        if n <= 0:
            return False
        log_n = math.log(n, 4)
        return log_n.is_integer()

        