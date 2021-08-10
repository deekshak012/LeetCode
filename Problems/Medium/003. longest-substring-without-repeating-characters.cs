public class Solution {
    public int LengthOfLongestSubstring(string s) {
        if(s==String.Empty)
            return 0;
        Dictionary<char,int> dict =new Dictionary<char,int>();
        int max=0;
        for(int i=0,j=0;i<s.Length;i++)
        {
            if(dict.ContainsKey(s[i]))
            {
                j = Math.Max(j,dict[s[i]]+1);
                dict[s[i]] = i;
            }
            else
                dict.Add(s[i],i);
            max = Math.Max(max,i-j+1);
        }
        return max;
    }
}

//My code - slow because of clear - v1
 // Dictionary<char,int> dict =new Dictionary<char,int>();
 //        int templen = 0, longestlen = 0;
 //        int len=0;
 //        while(len<s.Length)
 //        {
 //            if(dict.ContainsKey(s[len]))
 //            {
 //                len=dict[s[len]];
 //                if(templen > longestlen)
 //                    longestlen=templen;
 //                templen = 0;
 //                dict.Clear();
 //            }
 //            else
 //            {
 //                dict.Add(s[len],len);
 //                templen++;
 //            }
 //            if(templen > longestlen)
 //                    longestlen=templen;
 //            len++;
 //        }
 //        return longestlen;

