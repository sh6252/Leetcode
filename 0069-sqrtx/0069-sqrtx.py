class Solution:
    def mySqrt(self, x: int) -> int:
        n = 1
        ans = 0

        while n * n < x:
            n *= 2

        if n * n == x:
            return n

        right = n
        left = n // 2

        while left <= right:
            mid = (right + left) // 2
            if mid * mid < x:
                ans = mid
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else: 
                return mid
        
        return ans




        