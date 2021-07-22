
var isValid = function(s) {
    const a = new Map([['(', 1], ['[', 2], ['{', 3], [')', -1], [']', -2], ['}', -3]]);
    var arr=s.split``; var stack=[];
    for(i=0;i<arr.length;i++)
    {
        if(a.get(arr[i])>0) stack.push(arr[i])
        else {
            if(a.get(arr[i])*-1==a.get(stack[stack.length-1])) stack.pop()
            else
                return false;
        }
    }
    return stack.length==0? true: false;
};

