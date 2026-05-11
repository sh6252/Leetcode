class Solution:
    def separateNumber(self,number:int) -> List[int]:
        return [int(i) for i in str(number)]
    def separateDigits(self, nums: List[int]) -> List[int]:
        list_of_lists = list(map(self.separateNumber,nums))
        res = []
        for x in list_of_lists:
            for y in x:
                res.append(y)
        return res
        
        