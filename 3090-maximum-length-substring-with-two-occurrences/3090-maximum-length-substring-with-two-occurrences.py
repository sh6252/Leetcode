class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        dict_letters = {}
        max_length = 0

        for right in range(len(s)):
            letter = s[right]

            if letter not in dict_letters:
                dict_letters[letter] = 1

            elif dict_letters[letter] < 2:
                dict_letters[letter] += 1

            else:
                # letter appears for the 3rd time
                max_length = max(max_length, right - left)

                # Move left until we remove the previous
                # occurrence of 'letter'
                while s[left] != letter:
                    dict_letters[s[left]] -= 1
                    left += 1

                # Remove that previous occurrence too
                left += 1

        return max(max_length, len(s) - left)