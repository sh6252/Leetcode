class Solution {
public:
    int n;
    vector<int> suffix;
    vector<vector<int>> dp;

    int solve(int i, int M) {

        if (i == n)
            return 0;

        if (dp[i][M] != -1)
            return dp[i][M];

        int best = 0;

        for (int X = 1; X <= 2 * M && i + X <= n; X++) {

            int newM = max(M, X);

            int opponent = solve(i + X, newM);

            int current = suffix[i] - opponent;

            best = max(best, current);
        }

        return dp[i][M] = best;
    }

    int stoneGameII(vector<int>& piles) {
        n = piles.size();

        suffix.assign(n + 1, 0);

        for (int i = n - 1; i >= 0; i--) {
            suffix[i] = piles[i] + suffix[i + 1];
        }

        // dp[i][M]
        dp.assign(n + 1, vector<int>(n + 1, -1));

        return solve(0, 1);
    }
};