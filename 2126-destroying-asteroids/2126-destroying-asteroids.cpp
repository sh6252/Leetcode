class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        vector<int> cnt(100001, 0);

        for (int a : asteroids) {
            cnt[a]++;
        }

        long long currentMass = mass;

        for (int a = 1; a <= 100000; a++) {
            while (cnt[a]--) {
                if (currentMass < a) {
                    return false;
                }

                currentMass += a;
            }
        }

        return true;
    }
};