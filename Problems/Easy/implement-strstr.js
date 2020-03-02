var strStr = function(haystack, needle) {
    
    if (needle=="") return 0; 
        for (var i = 0; i <= haystack.length - needle.length; i++) {
            for (var j = 0; j < needle.length && haystack.charAt(i + j) == needle.charAt(j); j++)
                if (j == needle.length - 1) return i;
        }
        return -1;
   
};

/* MY APPROACH
var strStr = function(haystack, needle) {
    
    var index=-1; varj=1;
    if(needle.length==0) return 0;
    if(needle.length>haystack.length) return -1;
    for(var i=0;i<haystack.length;i++){
         if(needle[0]==haystack[i])
             {
                 var k=i+1;
                 
                 for(j=1;j<needle.length;j++)
                     { 
                     if(haystack[k]!= needle[j])
                         {
                             index=-1;
                             break;
                             
                         }
                         else k++;
                     }
                 if(j==needle.length)
                 {
                     index =i;
                     break;
                 }
             }
        
    }
    return index
   
};*/