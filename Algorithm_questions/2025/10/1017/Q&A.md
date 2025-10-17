| question                                                     | tag          |
| ------------------------------------------------------------ | ------------ |
| [不同路径](https://leetcode.cn/problems/unique-paths?envType=study-plan-v2&envId=top-100-liked) | 多维动态规划 |
| [最小路径和](https://leetcode.cn/problems/minimum-path-sum?envType=study-plan-v2&envId=top-100-liked) | 多维动态规划 |
| [最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring?envType=study-plan-v2&envId=top-100-liked) | 区间DP       |
| [最长公共子序列]()                                           | 两个数组的DP |
| [编辑距离](https://leetcode.cn/problems/edit-distance?envType=study-plan-v2&envId=top-100-liked) | 两个数组的DP |



## 不同路径

- 状态表示：`dp[i][j]`表示到达（i，j）位置不同的路径有多少条
- 状态转移方程：`dp[i][j] = dp[i-1][j] + dp[i][j-1]`
- 初始化，第一行和第一列都是1
- 填表顺序：从上向下，从左向右
- 返回值：`dp[m-1][n-1]`

```c++
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int> >dp(m,vector<int>(n));
        for(int j = 0;j<n;j++)dp[0][j] = 1;
        for(int i = 0;i<m;i++)dp[i][0] = 1;
        for(int i = 1;i<m;i++){
            for(int j = 1;j<n;j++){
                dp[i][j] = dp[i-1][j]+dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};
```

## 最小路径和

- 状态表示：`dp[i][j]`表示到达（i，j）位置的路径和的最小值
- 状态转移方程：`dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j] `
- 初始化：第一行和第一列
- 填表顺序：从上往下，从左往右
- 返回值：`dp[n-1][m-1]`

```c++
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int n = grid.size(),m = grid[0].size();
        vector<vector<int> >dp(n,vector<int>(m));
        dp[0][0] = grid[0][0];
        for(int j = 1;j<m;j++)dp[0][j]=dp[0][j-1]+grid[0][j];
        for(int i = 1;i<n;i++)dp[i][0] = dp[i-1][0]+grid[i][0];
        for(int i = 1;i<n;i++){
            for(int j = 1;j<m;j++)
            {
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j];
            }
        }
        return dp[n-1][m-1];
    }
};
```

## 最长回文子串

- 状态表示：`dp[i][j]`表示`[i,j]`区间是否是一个回文串
- 状态转移方程：见代码
- 初始化：无需初始化
- 填表顺序：从下往上，从左往右
- 返回值：最长的回文子串

```c++
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size(),b = 0,len = 0;
        vector<vector<bool> >f(n,vector<bool>(n));
        for(int i = n-1;i>=0;i--){
            for(int j = i;j<n;j++){
                if(s[i]==s[j]){
                    f[i][j] = (j-i<=1)?(s[i]==s[j]):f[i+1][j-1];
                    if(f[i][j]&&j-i+1>len){
                        b = i;
                        len = j-i+1;
                    }
                }
            }
        }
        return s.substr(b,len);
    }
};
```

## 最长公共子序列

- `dp[i][j]`表示字符串`s`的前`i`个字符和字符串`t`的前`j`个字符的最长公共子序列
- 状态转移方程：见代码
- 初始化：0个字符和任意个字符的公共子序列长度始终为`0`
- 填表顺序：从上往下，从左往右
- 返回值：`dp[n][m]`

```c++
class Solution {
public:
    int longestCommonSubsequence(string s, string t) {
        int n = s.size(),m = t.size();
        vector<vector<int> >dp(n+1,vector<int>(m+1));
        for(int i = 1;i<=n;i++){
            for(int j = 1;j<=m;j++){
                if(s[i-1]==t[j-1])dp[i][j] = dp[i-1][j-1]+1;
                else dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
            }
        }
        return dp[n][m];
    }
};
```

## 编辑距离

- 状态表示：`f[i][j]`表示字符串`a`的`[1,i]`区间，字符串`b`的`[1,j]`区间转换的最少操作数
- 状态转移方程：见代码
- 初始化：当一个字符串为空，想要转换只能删除/插入
- 填表顺序：从上往下，从左往右
- 返回值：`f[n][m]`

```c++
class Solution {
public:
    int minDistance(string a, string b) {
        int n = a.size(),m = b.size();
        vector<vector<int> >f(n+1,vector<int>(m+1));
        for(int i = 0;i<=n;i++)f[i][0] = i;
        for(int j = 0;j<=m;j++)f[0][j] = j;
        for(int i = 1;i<=n;i++){
            for(int j = 1;j<=m;j++){
                if(a[i-1]==b[j-1])f[i][j] = f[i-1][j-1];
                else{
                    f[i][j] = min(f[i-1][j-1],min(f[i-1][j],f[i][j-1]))+1;
                }
            }
        }
        return f[n][m];
    }
};
```

