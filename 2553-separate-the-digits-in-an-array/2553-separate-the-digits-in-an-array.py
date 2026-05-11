class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(d) for num in nums for d in str(num)]