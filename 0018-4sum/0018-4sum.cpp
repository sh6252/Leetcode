class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        int n = nums.size();
        if (n < 4) return result;

        sort(nums.begin(), nums.end());

        for (int i = 0; i < n - 3; i++) {
            // דילוג על כפילויות עבור i
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            // קיצור: הסכום המינימלי כבר גדול מהיעד
            if ((long long)nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target) break;
            // קיצור: הסכום המקסימלי עדיין קטן מהיעד
            if ((long long)nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target) continue;

            for (int j = i + 1; j < n - 2; j++) {
                // דילוג על כפילויות עבור j
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                if ((long long)nums[i] + nums[j] + nums[j+1] + nums[j+2] > target) break;
                if ((long long)nums[i] + nums[j] + nums[n-2] + nums[n-1] < target) continue;

                int left = j + 1, right = n - 1;

                while (left < right) {
                    long long sum = (long long)nums[i] + nums[j] + nums[left] + nums[right];

                    if (sum == target) {
                        result.push_back({nums[i], nums[j], nums[left], nums[right]});
                        // דילוג על כפילויות עבור left ו-right
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        return result;
    }
};