| question                                                     | tag               |
| ------------------------------------------------------------ | ----------------- |
| [和为k的子数组](https://leetcode.cn/problems/subarray-sum-equals-k?envType=study-plan-v2&envId=top-100-liked) | 哈希表+前缀和     |
| [滑动窗口的最大值]()                                         | 滑动窗口+单调队列 |
| [最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring?envType=study-plan-v2&envId=top-100-liked) | 哈希表+滑动窗口   |

## 和为k的子数组

- 使用**前缀和**处理整个数组
- 枚举右端点，存储左端点

```c++
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int>s(n);
        s[0]=nums[0];
        for(int i = 1;i<n;i++){
            s[i]=s[i-1]+nums[i];
        }
        unordered_map<int,int>cnt;
        cnt[0]=1;
        int ans = 0;
        for(int i = 0;i<n;i++){
            if(cnt.count(s[i]-k))ans+=cnt[s[i]-k];
            cnt[s[i]]++;
        }
        return ans;
    }
};
```

## 滑动窗口的最大值

- 从左向右维护固定长度区间的最大值的下标
- 单调队列，应当是单调递减的，保证最左边是最大值

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q =deque()
        for i,x in enumerate(nums):
            while q and nums[q[-1]]<=x:
                q.pop()
            q.append(i)
            if i-q[0]+1>k:
                q.popleft()
            if i>=k-1:
                ans.append(nums[q[0]])
        return ans
```

## 最小覆盖子串

- 先获取字符串`t`的信息，在遍历字符串`s`
- 滑动窗口得出答案
- 可优化点：不要每次都遍历一遍哈希表，而是储存有效的字符的个数

```c++
class Solution {
public:
    string minWindow(string s, string t) {
        int n = s.size();
        int cnt1[128]{},cnt2[128]{};
        for(char& c:t){
            cnt2[c]++;
        }
        int begin = -1,len = INT_MAX;
        auto check = [&cnt1,&cnt2]()->bool{
            for(int i = 0;i<128;i++){
                if(cnt1[i]<cnt2[i])return false;
            }
            return true;
        };
        for(int left = 0,right = 0;right<n;right++){
            cnt1[s[right]]++;
            while(left<=right&&check()){
                if(len>right-left+1){
                    begin = left,len=right-left+1;
                }
                cnt1[s[left++]]--;
            }
        }
        if(begin==-1)return "";
        else return s.substr(begin,len);
    }
};
```

优化版：

```C++
class Solution {
public:
    string minWindow(string s, string t) {
        int hash1[128] = {0};
        int kinds = 0;
        for(auto& ch :t){
            if(hash1[ch] == 0)
            {
                kinds++;
            }
            hash1[ch]++;
        }
        int hash2[128] = {0};
        int n = (int)s.size(),len = INT_MAX,begin = -1;

        for(int left = 0,right = 0,count = 0;right<n;right++)
        {
            char in = s[right];
            hash2[in]++;
            if(hash2[in] == hash1[in])count++;
            while(count == kinds){
                if(len>right-left+1)
                {
                    len = right-left+1;
                    begin = left;
                }
                char out = s[left++];
                if(hash2[out]==hash1[out])count--;
                hash2[out]--;
                
            }

        }
        if(begin == -1)return "";
        return s.substr(begin,len);
    }
};
```

