class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = dict()
        right = 0
        left = 0
        max_length = 0
        len_str = len(s)

        if len_str < 2:
            return len_str
        
        while right < len_str:
            if s[right] in letters.keys():
                max_length = max(right - left, max_length)
                left = letters[s[right]] + 1
                right = left
                letters = dict()
            else:
                letters[s[right]] = right
                max_length = max(right - left + 1, max_length)
                right+=1
                
        
        return max_length
        

        


            

        