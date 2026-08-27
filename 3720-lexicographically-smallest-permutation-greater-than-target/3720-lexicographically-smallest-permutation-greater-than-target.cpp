class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.size();

        // Step 1: count letters available in s
        array<int,26> cnt{};
        for (char c : s) cnt[c - 'a']++;

        // Step 2: "tight" pass - try to match target as long as possible,
        // storing a snapshot of the counts BEFORE using each position's letter
        vector<array<int,26>> snapshot(n + 1);
        snapshot[0] = cnt;

        int L = 0; // length of the tight match with target
        while (L < n) {
            int c = target[L] - 'a';
            if (cnt[c] > 0) {
                cnt[c]--;
                L++;
                snapshot[L] = cnt;
            } else break; // can't match target[L], tight match stops here
        }

        // Step 3: decide where to start searching for a break point
        // If L == n, s can exactly reproduce target -> not strictly greater,
        // so we must break somewhere before the last position (n-1)
        int start = (L == n) ? n - 1 : L;

        // Step 4: search for the rightmost feasible break point, from start down to 0
        for (int i = start; i >= 0; i--) {
            array<int,26>& state = snapshot[i]; // counts available at this position
            int t = target[i] - 'a';
            int chosen = -1;
            // find the smallest letter strictly greater than target[i] that's available
            for (int c = t + 1; c < 26; c++) {
                if (state[c] > 0) { chosen = c; break; }
            }
            if (chosen == -1) continue; // no valid letter here, try an earlier position

            // Step 5: build the answer
            // positions 0..i-1: copy exactly from target (tight prefix)
            string ans(n, ' ');
            for (int k = 0; k < i; k++) ans[k] = target[k];

            // position i: the chosen greater letter
            ans[i] = 'a' + chosen;

            // remaining letters after using "chosen"
            array<int,26> rem = state;
            rem[chosen]--;

            // fill positions i+1..n-1 with remaining letters in ascending order
            // (smallest possible arrangement)
            int idx = i + 1;
            for (int c = 0; c < 26; c++)
                for (int k = 0; k < rem[c]; k++)
                    ans[idx++] = 'a' + c;

            return ans;
        }

        // no valid break point found anywhere -> no permutation of s is > target
        return "";
    }
};