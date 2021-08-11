public class Solution {
    public int MissingNumber(int[] nums) {
        int max= nums.Length;
        int sum= max * (max+1) / 2;
        for(int i = 0; i< max ;i++)
            sum-=nums[i];
        return sum;   
    }
}