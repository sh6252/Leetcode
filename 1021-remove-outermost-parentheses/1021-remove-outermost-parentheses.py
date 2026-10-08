class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        cnt = 0

        for c in s:
            if c == ")":
                if cnt > 1:
                    res += c
                cnt -= 1
            else:
                if cnt > 0:
                    res += c
                cnt += 1

        return res  
                

                    
        