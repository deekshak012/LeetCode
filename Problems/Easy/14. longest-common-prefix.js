var longestCommonPrefix = function(str) {
    if(str.length<=0) return "";
    var i=0;var result=[];
    var length=str.reduce((a, b) => a.length <= b.length ? a : b).length;    
    while(i<=length)
    {
           if(str.every(x => x.charAt(i) == str[0].charAt(i))){
               result.push(str[0].charAt(i));
           }
            else break;
        i++;
    }
    return result.join``;
};