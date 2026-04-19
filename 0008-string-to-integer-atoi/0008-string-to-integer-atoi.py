class Solution:

    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        result = 0

        while i < n and s[i] == ' ':
            i += 1

        if i < n and s[i] in "+-":
            sign = -1 if s[i] == '-' else 1
            i += 1

            if i < n and s[i] in "+-":   # <- תיקון חשוב
                return 0

        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        if result > self.INT_MAX:
            return self.INT_MAX
        if result < self.INT_MIN:
            return self.INT_MIN

        return result