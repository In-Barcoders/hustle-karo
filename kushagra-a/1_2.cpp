class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) 
    {
       
       vector<vector<int>> res;
        int n=nums.size();
        sort(nums.begin(),nums.end());
        
        if(n<3)
            return res;
        for(int i=0;i<n-2;i++)
        {
            if(i==0 ||(i>0 && nums[i]!=nums[i-1])) 
            {    
                int low=i+1,high=n-1;
                while(low<high)
                {
                    int sum=nums[i]+nums[low]+nums[high];
                    if(sum==0)
                    {
                        res.push_back({nums[i],nums[low],nums[high]});                                   
                        while(low<high && nums[low]==nums[low+1])low++;
                        while(low<high && nums[high]==nums[high-1])high--;
                        low++;high--;
                    }
                    if(sum>0)high--;
                    if(sum<0)low++;
                }
            }
        }
        return res;
            
    }
};