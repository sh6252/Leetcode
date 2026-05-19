class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        intersection = list(set(nums1) & set(nums2))
        if len(intersection) == 0:
            return -1
        else:
            return min(intersection)

        