#### 跳台阶扩展问题

- **题目链接**：[跳台阶扩展问题](https://www.nowcoder.com/practice/953b74ca5c4d44bb91f39ac4ddea0fee?tpId=230&tqId=39750&ru=/exam/oj)
- **难度**：⭐⭐
- **标签**：`动态规划`、`找规律`

#### 💡 题目描述

一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级…… 它也可以跳上 n 级。求该青蛙跳上一个 n 级的台阶（n 为正整数）总共有多少种跳法。
数据范围：1≤n≤20
进阶：空间复杂度 O (1)，时间复杂度 O (1)

示例1
输入

```
3
```

输出

```
4
```
示例2
输入

```
1
```

输出

```
1
```

#### 思路分析

求该青蛙跳上一个 n 级的台阶（n 为正整数）总共有多少种跳法。

 - 🧠  **算法分析**：
   

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b90a8e3384aa4f52abf1fbb2a42a94cf.png)

查看图片即可

2. ⚡ **代码实现**：

```cpp
// cpp版本
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin>>n;
    cout<<(1<<(n-1))<<endl;
    return 0;
}
```

---
#### 包含不超过两种字符的最长子串

- **题目链接**：[包含不超过两种字符的最长子串](https://www.nowcoder.com/practice/90d6a362fa7d4c519d557da797bb02ce?tpId=196&tqId=40552&ru=/exam/oj)
- **难度**：⭐⭐
- **标签**：`双指针`、`滑动窗口`

#### 💡 题目描述

给定一个长度为 n 的字符串，找出最多包含两种字符的最长子串 t，返回这个最长的长度。
数据范围：1≤n≤10⁵，字符串仅包含小写英文字母。

示例1
输入

```
nowcoder
```

输出

```
2
```
示例2
输入

```
nooooow
```

输出

```
6
```

#### 思路分析

最长的长度

 - 🧠  **算法分析**：
   

标准的滑动窗口（双指针）问题

⚡ **代码实现**：

```cpp
// cpp版本
#include <iostream>
#include <ostream>
#include <string>
using namespace std;
int cnt[26];

bool check()
{
    int ans = 0;
    for (const int& x : cnt)
        if (x)
            ++ans;
    return ans > 2;
}
int main() {
    string s;
    cin>>s;
    int n = s.size(),ret = 1;
    for(int left = 0,right = 0;right<n;right++){
        int in = s[right]-'a';
        cnt[in]++;
        while(check()){
            int out = s[left++]-'a';
            cnt[out]--;
        }
        ret = max(ret,right-left+1);
    }
    cout<<ret<<endl;
    return 0;
}
// 64 位输出请用 printf("%lld")
```
---
#### 字符串的排列

- **题目链接**：[字符串的排列](https://www.nowcoder.com/practice/fe6b651b66ae47d7acce78ffdd9a96c7?tpId=13&tqId=11180&ru=/exam/oj)
- **难度**：⭐⭐⭐
- **标签**：`搜索`

#### 💡 题目描述

输入一个长度为 n 的字符串，打印出该字符串中字符的所有排列，你可以以任意顺序返回这个字符串数组。例如：输入字符串 "ABC"，则输出由字符 A,B,C 所能排列出来的所有字符串 ["ABC","ACB","BAC","BCA","CBA","CAB"]。
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/51585e8754b940b1b31445ac4a55641f.png)

数据范围：n < 10要求：空间复杂度 O(n!)，时间复杂度 O(n!)

示例1
输入

```
"ab"
```

输出

```
["ab","ba"]
```
示例2
输入

```
"aab"
```

输出

```
["aab","aba","baa"]
```
示例3
输入

```
"abc"
```

输出

```
["abc","acb","bac","bca","cab","cba"]
```
#### 思路分析

任意顺序返回这个字符串数组

 - 🧠  **算法图解**：
   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/47e50b5127f14fe09f11bb11838c939d.png)

如图

⚡ **代码实现**：

```cpp
// cpp版本
class Solution {
    vector<string>ret;
    int n;
    string path;
    vector<bool>vis;
    void dfs(const string& str,int u){
        if(u==n){
            ret.emplace_back(path);
            return;
        }
        for(int i=0;i<n;i++){
            if(i>0&&str[i]==str[i-1]&&!vis[i-1])continue;
            if(!vis[i]){
                vis[i]=true;
                path.push_back(str[i]);
                dfs(str,u+1);
                vis[i]=false;
                path.pop_back();
            }
        }
    }
public:
    vector<string> Permutation(string str) {
        // write code here
        n = str.size();
        sort(str.begin(),str.end());
        vis.resize(n);
        dfs(str,0);
        return ret;
    }
};
```

---
