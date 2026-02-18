class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        for(int i=0; i<nums.length-3;i++){
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for(int j = i+1;j<nums.length-2;j++){
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                long newTarget = (long) target - nums[i] - nums[j];
                int start = j + 1, end = nums.length - 1;
                while(start < end){
                    if((long)(nums[start] + nums[end]) == newTarget){
                        ans.add(Arrays.asList(nums[i], nums[j], nums[start], nums[end]));
                        while(start < end && nums[end-1] == nums[end])end--;
                        while(start < end && nums[start+1] == nums[start])start++;
                        end--;
                        start++;
                    }
                    else{
                        if((long)(nums[start] + nums[end]) > newTarget){
                            end--;
                        }else{
                            start++;
                        }
                    }
                }
            }
        }
        return ans;
    }
}