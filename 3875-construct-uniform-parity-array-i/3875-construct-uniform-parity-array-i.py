class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True
        n = len(nums1)
        odd = 0
        even = 0

        for num in nums1:
            odd += num % 2
            even += (1 - num % 2)
        
        return odd == 0 or even == 0 or odd >= 2 or even >= 1
        