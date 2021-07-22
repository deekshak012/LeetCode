public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> hash = new Dictionary<int, int>();
        int i;
        for(i=0;i<nums.Length;i++)
        {
            if(hash.ContainsKey(target - nums[i]))
                return new int[] {hash[target-nums[i]],i};
            else    
                hash.Add(nums[i],i);
            
        }
        return new int[]{};
    }
}