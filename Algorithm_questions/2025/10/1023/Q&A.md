| question                                                     | tag      |
| ------------------------------------------------------------ | -------- |
| [添加逗号_牛客题霸_牛客网](https://www.nowcoder.com/practice/f51c317e745649c0900996fd3f683aed?tpId=290&tqId=39934&ru=/exam/oj) | 枚举     |
| [跳台阶_牛客题霸_牛客网](https://www.nowcoder.com/practice/bfb2a2b3cdbd4bd6bba0d4dca69aa3f0?tpId=230&tqId=39749&ru=/exam/oj) | 动态规划 |
| [扑克牌顺子_牛客题霸_牛客网](https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4?tpId=13&tqId=11198&ru=/exam/oj) | 找规律   |
| [最长回文子串_牛客题霸_牛客网](https://www.nowcoder.com/practice/b4525d1d84934cf280439aeecc36f4af?tpId=182&tqId=34752&ru=/exam/oj) | 动态规划 |
| [买卖股票的最好时机(一)_牛客题霸_牛客网](https://www.nowcoder.com/practice/351b87e53d0d44928f4de9b6217d36bb?tpId=230&tqId=39767&ru=/exam/oj) | 贪心     |
| [[NOIP2002 普及组\] 过河卒_牛客题霸_牛客网](https://www.nowcoder.com/practice/cc1a9bc523a24716a117b438a1dc5706?tpId=230&tqId=40428&ru=/exam/oj) | 动态规划 |



## [添加逗号_牛客题霸_牛客网](https://www.nowcoder.com/practice/f51c317e745649c0900996fd3f683aed?tpId=290&tqId=39934&ru=/exam/oj)

```c++
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cin>>s;
    string result = "";

    int count = 0;
    // 从后往前遍历字符串
    for (int i = s.length() - 1; i >= 0; i--) {
        result += s[i];
        count++;

        // 每3位数字插入一个逗号，但不是在最后一位
        if (count % 3 == 0 && i != 0) {
            result += ",";
        }
    }

    // 反转结果字符串，因为我们是从后往前构建的
    reverse(result.begin(), result.end());

    cout << result << endl;

    return 0;
}
```

## [跳台阶_牛客题霸_牛客网](https://www.nowcoder.com/practice/bfb2a2b3cdbd4bd6bba0d4dca69aa3f0?tpId=230&tqId=39749&ru=/exam/oj)

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin>>n;
    vector<int>f(n+1);
    //f[i] = f[i-1]+f[i-2]
    f[1] = f[0] = 1;
    for(int i = 2;i<=n;i++)f[i] = f[i-1]+f[i-2];
    cout<<f[n]<<endl;
    return 0;
}
// 64 位输出请用 printf("%lld")
```

## [扑克牌顺子_牛客题霸_牛客网](https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4?tpId=13&tqId=11198&ru=/exam/oj)

- 最大和最小数的差不会超过4
- 没有重复的元素

```c++
class Solution {
    bool hash[14] = { 0 };
  public:
    bool IsContinuous(vector<int>& numbers) {
        int maxVal = 0, minVal = 14;
        for (auto x : numbers) {
            if (x) {
                if (hash[x]) return false;
                hash[x] = true;
                maxVal = max(maxVal, x);
                minVal = min(minVal, x);
            }
        }
        return maxVal - minVal <= 4;
    }
};
```

## [最长回文子串_牛客题霸_牛客网](https://www.nowcoder.com/practice/b4525d1d84934cf280439aeecc36f4af?tpId=182&tqId=34752&ru=/exam/oj)

```c++
class Solution {
public:
    int getLongestPalindrome(string s) {
        // write code here
        int n = s.size();
        vector<vector<bool> >f(n,vector<bool>(n));
        int len = 1;
        for(int i = n-1;i>=0;i--){
            for(int j = i;j<n;j++){
                if(s[i]==s[j]){
                    f[i][j] = (j - i <= 1) ? (s[i] == s[j]) : f[i + 1][j - 1];
                    if(f[i][j]&&j-i+1>len)len = j-i+1;
                }
            }
        }
        return len;
    }
};
```

## [买卖股票的最好时机(一)_牛客题霸_牛客网](https://www.nowcoder.com/practice/351b87e53d0d44928f4de9b6217d36bb?tpId=230&tqId=39767&ru=/exam/oj)

- 维护一个最小值

```c++
#include <climits>
#include <iostream>
using namespace std;

int main() {
    int minVal = INT_MAX;
    int n;
    cin>>n;
    int ret = 0;
    for(int i = 0;i<n;i++){
        int x;
        cin>>x;
        ret = max(ret,x-minVal);
        minVal = min(x,minVal);
    }
    cout<<ret<<'\n';
    return 0;
}
// 64 位输出请用 printf("%lld")
```

## [[NOIP2002 普及组\] 过河卒_牛客题霸_牛客网](https://www.nowcoder.com/practice/cc1a9bc523a24716a117b438a1dc5706?tpId=230&tqId=40428&ru=/exam/oj)

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m, x, y;
    cin >> n >> m >> x >> y;

    vector<vector<bool>> blocked(n + 1, vector<bool>(m + 1, false));
    
    // 马的位置和8个控制点
    int dx[] = {0, 1, 1, -1, -1, 2, 2, -2, -2};
    int dy[] = {0, 2, -2, 2, -2, 1, -1, 1, -1};
    for (int i = 0; i < 9; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx >= 0 && nx <= n && ny >= 0 && ny <= m) {
            blocked[nx][ny] = true;
        }
    }
    vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, 0));
    if (!blocked[0][0]) {
        dp[0][0] = 1;
    }
    for (int i = 1; i <= n; i++) {
        if (!blocked[i][0]) {
            dp[i][0] = dp[i - 1][0];
        }
    }
    for (int j = 1; j <= m; j++) {
        if (!blocked[0][j]) {
            dp[0][j] = dp[0][j - 1];
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (!blocked[i][j]) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
    }
    cout << dp[n][m] << endl;
    return 0;
}
```

