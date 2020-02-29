var romanToInt = function(s) {
    const pref = new Map([['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100], ['D', 500], ['M', 1000]]);
    var a=s.split``; var result=0;
    for(var i=0;i<a.length;i++)
    {
         pref.get(a[i])<pref.get(a[i+1])? result-=pref.get(a[i]): result+=pref.get(a[i]);         
    }
    return result;
};