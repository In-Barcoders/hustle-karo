class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) 
    {
        sort(strs.begin(),strs.end());
        int s=strs.size();
        if(s==0)
            return "";
        string pre="";
        for (int i=0,j=0;i<strs[0].size()&&j<strs[s-1].size();i++,j++)
        {
            if(strs[0][i]==strs[s-1][j])
            {
                pre+=strs[0][i];
            }
            else
            {
                break;
            }
        }
        return pre;
    }
};