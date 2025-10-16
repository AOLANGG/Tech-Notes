| question                                                     | tag      |
| ------------------------------------------------------------ | -------- |
| [单词拆分](https://leetcode.cn/problems/word-break?envType=study-plan-v2&envId=top-100-liked) | 动态规划 |
| [最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence?envType=study-plan-v2&envId=top-100-liked) | 动态规划 |
| [乘积最大的子数组](https://leetcode.cn/problems/maximum-product-subarray?envType=study-plan-v2&envId=top-100-liked) | 动态规划 |
| [分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum?envType=study-plan-v2&envId=top-100-liked) | 动态规划 |
| [最长有效括号](https://leetcode.cn/problems/longest-valid-parentheses?envType=study-plan-v2&envId=top-100-liked) | 动态规划 |

## 单词拆分

- 状态表示：dp[i]表示前i个字符是否可以由字典中的单词拼接而成
- 状态转移方程：见代码
- 初始化：`dp[0]=true`，我们加入了一个“空”的字符，用来统一下标
- 填表顺序：从左向右
- 返回值：前n个字符是否可以由字典中的单词拼接而成——`dp[n]`

```c++
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        unordered_set<string>hash;
        for(auto&ss:wordDict)
            hash.insert(ss);
        s = ' '+s;
        vector<bool>dp(n+1);
        dp[0] = true;
        for(int i = 1;i<=n;i++)
        {
            for(int j = i;j>0;j--)
            {
                if(dp[j-1]&&hash.count(s.substr(j,i-j+1)))
                {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
};
```

## 最长递增子序列

- 状态表示：`dp[i]`表示以第`i`个字符结尾的最长杨哥递增子序列的长度
- 状态转移方程：见代码
- 初始化：`dp`表全为1
- 填表顺序：从左向右
- 返回值：`dp[n]`

```c++
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int ans = 1,n = nums.size();
        vector<int>dp(n,1);
        for(int i = 0;i<n;i++){
            for(int j = 0;j<i;j++)
            {
                if(nums[j]<nums[i]){
                    dp[i] = max(dp[i],dp[j]+1);
                    ans=max(dp[i],ans);
                }
            }
        }
        return ans;
    }
};
```

## 乘积最大的子数组

- 状态表示：`f[i]`表示前`i`个元素中的最大的子数组乘积，`g[i]`表示前`i`个元素中最小的子数组乘积
- 状态转移方程：见代码
- 初始化：初始化第一个数同时为最大值和最小值
- 填表顺序：从左向右
- 返回值：`ret`

```c++
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        vector<int>f(n);
        auto g = f;
        int ret = g[0] = f[0] = nums[0];
        for(int i = 1;i<n;i++){
            f[i]=max(nums[i],max(f[i-1]*nums[i],g[i-1]*nums[i]));
            g[i]=min(nums[i],min(f[i-1]*nums[i],g[i-1]*nums[i]));
            ret = max(ret,f[i]);
        }
        return ret;
    }
};
```

## 分割等和子集

- 状态表示：`dp[i][j]`表示从前i个元素中挑选，总和为j的情况是否存在
- 状态转移方程：`dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i-1]]`
- 初始化：前0个元素中挑选，总和只能是0
- 填表顺序：从上往下，从左往右（优化之后应该是从右向左）
- 返回值：`dp[target]`

```c++
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size(),sum = 0;
        for(int&x:nums)sum+=x;
        if(sum%2)return false;
        int target = sum/2;
        vector<bool>dp(target+1);
        // dp[i][j]表示从前i个元素中挑选，总和为j的情况是否存在
        dp[0] = true;
        for(int i = 1;i<=n;i++)
        {
            for(int j = target;j>=nums[i-1];j--)
            {
                dp[j] = dp[j] || dp[j-nums[i-1]];
            }
        }
        return dp[target];
    }
};
```

## 最长有效括号

- 状态表示：`dp[i]`表示以`s[i]`结尾的最长有效括号子串的长度
- 状态转移方程：见代码
- 初始化：不需要
- 填表顺序：从左向右
- 返回值：`ans`

```c++
class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.size();
        vector<int> dp(n);
        int ans = 0;
        for (int i = 1; i < n; i++) {
            if (s[i] == ')') {
                if (s[i - 1] == '(') {
                    dp[i] = (i - 2 >= 0) ? dp[i - 2] + 2 : 2;
                } else {
                    int m = i - dp[i - 1] - 1;
                    if (m >= 0 && s[m] == '(') {
                        dp[i] = dp[i - 1] + 2;
                        if (m - 1 >= 0) {
                            dp[i] += dp[m - 1];
                        }
                    }
                }
                ans = max(ans, dp[i]);
            }
        }
        return ans;
    }
};
```

