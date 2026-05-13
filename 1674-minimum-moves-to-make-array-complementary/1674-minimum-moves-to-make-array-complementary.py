class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)

        # diff[s] = שינוי בעלות החל מ־s
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b)
            high = max(a, b)

            # =========================
            # בהתחלה מניחים:
            # כל S עולה 2
            # =========================

            # טווח של 1 move:
            # [low+1, high+limit]

            diff[low + 1] -= 1
            diff[high + limit + 1] += 1

            # בנקודה של 0 moves:
            # S = a+b

            s = a + b

            diff[s] -= 1
            diff[s + 1] += 1

        # =========================
        # מתחילים מכל זוג בעלות 2
        # =========================

        current = n
        ans = float('inf')

        for s in range(2, 2 * limit + 1):
            current += diff[s]
            ans = min(ans, current)

        return ans