class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        great = []
        cnt_eq = 0
        for n in nums:
            if n == pivot:
                cnt_eq += 1
            elif n < pivot:
                less.append(n)
            else:
                great.append(n)
        return less + [pivot]*cnt_eq + great
        