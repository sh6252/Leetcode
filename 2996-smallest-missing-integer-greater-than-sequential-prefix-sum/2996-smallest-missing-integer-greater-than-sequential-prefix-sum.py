class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        # Find the sum of the sequential prefix
        prefix_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                break
            prefix_sum += nums[i]

        # Find the smallest missing integer greater than prefix_sum
        nums_set = set(nums)
        answer = prefix_sum

        while answer in nums_set:
            answer += 1

        return answer