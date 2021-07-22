/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public TreeNode SortedArrayToBST(int[] nums) {
        return SortedArrayToBST(nums, 0, nums.Length-1);
    }
    public TreeNode SortedArrayToBST(int[] nums, int lo, int hi){
        if(lo > hi)
            return null;
        int mid = (hi-lo)/2+lo;
        TreeNode root = new TreeNode(nums[mid]);
        root.left =  SortedArrayToBST(nums, lo, mid-1);
        root.right =  SortedArrayToBST(nums, mid+1, hi);
        return root;
}
}