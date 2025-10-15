| question                                                     | tag          |
| ------------------------------------------------------------ | ------------ |
| [爬楼梯](https://leetcode.cn/problems/climbing-stairs?envType=study-plan-v2&envId=top-100-liked) | 动态规划     |
| [杨辉三角](https://leetcode.cn/problems/pascals-triangle?envType=study-plan-v2&envId=top-100-liked) | 动态规划     |
| [打家劫舍](https://leetcode.cn/problems/house-robber?envType=study-plan-v2&envId=top-100-liked) | 动态规划     |
| [完全平方数](https://leetcode.cn/problems/perfect-squares?envType=study-plan-v2&envId=top-100-liked) | 完全背包问题 |
| [零钱兑换](https://leetcode.cn/problems/coin-change?envType=study-plan-v2&envId=top-100-liked) | 完全背包问题 |



## 爬楼梯

- 每次可以爬`1`或`2`个台阶。可以理解状态转移方程为`dp[i]=dp[i-1]+dp[i-2]`

```c++
class Solution {
public:
    int climbStairs(int n) {
        if(n==1)return 1;
        vector<int>dp(n+1);
        dp[1] = 1;
        dp[2] = 2;
        for(int i = 3;i<=n;i++)
        {
            dp[i] = dp[i-1]+dp[i-2];
        }
        return dp[n];
    }
};
```

## 杨辉三角

- 状态转移方程为`dp[i][j] = dp[i-1][j-1]+dp[i-1][j]`，再注意边界条件

```c++
class Solution {
public:
    vector<vector<int>> generate(int n) {
        vector<vector<int> >dp(n);
        //分为两步来填充
        for(int i = 0;i<n;++i)
        {
            dp[i].resize(i+1);
            dp[i][0] = dp[i][i] = 1;
        }
        
        for(int i = 2;i<n;++i)
        {
            for(int j = 1;j<i;++j)
            {
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j];
            }
        }
        return dp;
    }
};
```

## 打家劫舍

- 定义两个`dp表`，每个位置考虑偷或者不偷
  - `f[i]`：表示第`i`个位置偷的条件下，前`i`个元素的最高金额
  - `g[i]`：表示第`i`个位置不偷的条件下，前`i`个元素的最高金额

```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        vector<int>f(n);
        auto g = f;
        f[0] = nums[0];
        for(int i = 1;i<n;i++)
        {
            f[i]=g[i-1]+nums[i];
            g[i] = max(f[i-1],g[i-1]);
        }
        return max(f[n-1],g[n-1]);
    }
};
```

## 完全平方数

- 状态表示：`dp[i][j]`表示前`i`个完全平方数中，和为`j`的最小的数量
- 状态转移方程：`dp[i][j]=min(dp[i-1][j],dp[i][j-i*i]+1)`
- 初始化，前0个完全平方数只能弄出一个0，其余数都初始化为无穷大
- 填表顺序：从上向下，从左向右
- 返回结果：`dp[m][n]`——前`m`个完全平方数中，和为`n`的最小的数量

```c++
class Solution {
public:
    int numSquares(int n) {
        int m = sqrt(n);
        vector<vector<int> >dp(m+1,vector<int>(n+1));
        // dp[i][j]表示前i个完全平方数中，和为j的最小的数量
        for(int j = 1;j<=n;j++)
            dp[0][j] = 0x3f3f3f3f;
        for(int i = 1;i<=m;i++){
            for(int j = 1;j<=n;j++){
                dp[i][j] = dp[i-1][j];
                if(j>=i*i)
                    dp[i][j] = min(dp[i][j],dp[i][j-i*i]+1);
            }
        }
        return dp[m][n];
    }
};
```



## 零钱兑换

- 状态表示：`dp[i][j]`表示前i个硬币，总金额为j，的最少硬币个数
- 状态转移方程：`dp[i][j] = min(dp[i][j],dp[i][j-coins[i-1]]+1)`
- 初始化：前0个硬币只能弄出一个0，其余数都初始化为无穷大
- 填表顺序：从上向下，从左向右
- 返回值：`dp[n`][amount]

```c++
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        vector<vector<int> >dp(n+1,vector<int>(amount+1));
        // dp[i][j]表示前i个硬币，总金额为j，的最少硬币个数
        for(int j = 1;j<=amount;j++)
            dp[0][j] = 0x3f3f3f3f;
        for(int i = 1;i<=n;i++){
            for(int j = 1;j<=amount;j++)
            {
                dp[i][j] = dp[i-1][j];
                if(j>=coins[i-1])
                    dp[i][j] = min(dp[i][j],dp[i][j-coins[i-1]]+1);
            }
        }
        return dp[n][amount]==0x3f3f3f3f?-1:dp[n][amount];
    }
};
```

