/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if(n==0)return 0
    if(n==1)return 1
    if(n==2)return 2
    var prev_no=1,prev_2_no=2,all=0;
    for(var i=3;i<=n;i++)
        {
            all=prev_no+prev_2_no;
            prev_no=prev_2_no;
            prev_2_no=all;
        }
    return all;
};