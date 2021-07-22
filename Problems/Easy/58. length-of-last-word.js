/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {  
    var a=s.trim().split(' ');
    return a[a.length-1].length
};

/*
var lengthOfLastWord = function(s) {  
    s=s.trim()
    var lastindex= length=s.length;      
    while(lastindex!=0 && s.charAt(lastindex-1)!=' ')
    lastindex--
    return length-lastindex;
};*/