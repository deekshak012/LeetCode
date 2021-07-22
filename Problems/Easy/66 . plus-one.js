/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    l=digits.length;
    ++digits[l-1];
    while(--l>=0)
    {
       
        if(digits[l] <= 9  ) break;
        else {
            digits[l]=0
            l==0? digits = [1].concat(digits) : digits[l-1]++
            
        }
    }  
    return digits
};
