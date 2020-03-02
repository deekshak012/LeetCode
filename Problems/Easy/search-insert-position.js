
var searchInsert = function(nums, target) {
   var h=nums.length-1,l=0,m=0
   while(l<=h){
       m=Math.floor((l+h)/2)
       if(nums[m]==target)
           return m
       else if (nums[m]>target)
          h=m-1
       else 
           l=m+1
           
   }
    return l   
};//O(logn)



/* My old approach
var searchInsert = function(nums, target) {
    var index = nums.indexOf(target) ; 
    
    if(index>-1)return index;
    for(var i=0;i<nums.length;i++)
        if(target<nums[i])return i;
    return nums.length
};*/