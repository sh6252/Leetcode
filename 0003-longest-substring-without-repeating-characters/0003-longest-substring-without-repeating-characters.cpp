class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> letters;  // השתמשתי ב-unordered_map למהירות (O(1) בממוצע)
        int len = s.length();
        int max_len = 0;
        int begin_i = 0;

        for (int i = 0; i < len; i++) {
            letters[s[i]]++;  // תמיד הוסף את התו הנוכחי

            while (letters[s[i]] > 1) {  // אם כפול, הזז את begin_i עד שהכפילות נעלמת
                letters[s[begin_i]]--;
                begin_i++;
            }

            max_len = max(max_len, i - begin_i + 1);  // עדכן בכל איטרציה!
        }

        return max_len;
    }
};