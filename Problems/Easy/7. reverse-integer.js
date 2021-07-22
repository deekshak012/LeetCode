var reverse = function(x) {
    var rev= parseInt(Math.abs(x).toString().split``.reverse().join(''))
    return rev>2**31?0:rev*Math.sign(x);
};