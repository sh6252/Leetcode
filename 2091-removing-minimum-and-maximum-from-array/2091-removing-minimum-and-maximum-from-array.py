class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        min_val = min(nums)
        max_val = max(nums)

        left = n
        right = -1

        for i in range(n):
            if nums[i] == min_val or nums[i] == max_val:
                left = min(left, i)
                right = max(right, i)

        remove_left = right + 1
        remove_right = n - left
        remove_both = left + 1 + n - right

        return min(remove_left, remove_right, remove_both)