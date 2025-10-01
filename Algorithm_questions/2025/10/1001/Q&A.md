| question                                                     | tag    |
| ------------------------------------------------------------ | ------ |
| [最大子数组和](https://leetcode.cn/problems/maximum-subarray?envType=study-plan-v2&envId=top-100-liked) | 贪心   |
| [合并区间](https://leetcode.cn/problems/merge-intervals?envType=study-plan-v2&envId=top-100-liked) | 排序   |
| [轮转数组](https://leetcode.cn/problems/rotate-array?envType=study-plan-v2&envId=top-100-liked) | 双指针 |



## 最大子数组和

- 遍历的同时记录和，如果和<0，那么对于后面的数来说就是拖后腿的，这时候就需要及时止损。
- 相反，如果>=0，则对后面的数据有帮助（0的时候无影响），则继续保留

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n,ans = len(nums),-inf
        sum = 0
        for i,x in enumerate(nums):
            if sum < 0:
                sum = 0
            sum += x
            ans = max(ans,sum)
        return int(ans)
```



## 合并区间

- 对左端点进行排序即可

```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int> >ans;
        int n = intervals.size();
        sort(intervals.begin(),intervals.end());
        int left = intervals[0][0],right = intervals[0][1];
        for(int i = 1;i<n;i++){
            if(intervals[i][0]<=right)right=max(right,intervals[i][1]);
            else{
                ans.push_back({left,right});
                left=intervals[i][0],right=intervals[i][1];
            }
        }
        ans.push_back({left,right});
        return ans;
    }
};
```

## 轮转数组

- 三步反转法

```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k%=nums.size();
        reverse(nums.begin(),nums.end());
        reverse(nums.begin(),nums.begin()+k);
        reverse(nums.begin()+k,nums.end());
    }
};
```

