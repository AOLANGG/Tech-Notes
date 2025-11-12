#### 游游的字母串

- **题目链接**：[游游的字母串](https://ac.nowcoder.com/acm/problem/255195)
- **难度**：⭐⭐
- **标签**：`模拟`

#### 💡 题目描述
对于一个小写字母而言，游游可以通过一次操作把这个字母变成相邻的字母。'a'和'b'相邻，'b'和'c'相邻，以此类推。特殊的，'a'和'z'也是相邻的。可以认为，小写字母的相邻规则为一个环。
游游拿到了一个仅包含小写字母的字符串，她想知道，使得所有字母都相等至少要多少次操作？


示例1
输入

```
yab
```

输出

```
3
```


#### 思路分析

 - 🧠  **算法分析**：
本题较为简单，直接   


2. ⚡ **代码实现**：

```cpp
// cpp版本
#include <iostream>
#include <string>
#include <climits>
#include <cmath>

using namespace std;

int main(){
    string s;
    cin>>s;
    int ret = INT_MAX;
    for(int c = 'a';c<='z';c++){
        int sum = 0;
        for(const char&ch:s){
            sum += min(26-abs(c-ch),abs(c-ch));
        }
        ret = min(ret,sum);
    }
    cout<<ret<<endl;
    return 0;
}
```

---
#### 体育课测验(二)

- **题目链接**：[体育课测验(二)](https://www.nowcoder.com/practice/64a4c026b2aa4411984f560deec36323?tpId=196&tqId=40272&ru=/exam/oj)
- **难度**：⭐⭐
- **标签**：`拓扑排序`

#### 💡 题目描述
体育课共有 numProject 个考核项目，编号为 0 到 numProject - 1。考核中，每两个项目被划分为一组，形成分组数组 groups（数组中的每个元素 groups[i] 是一个包含两个项目的子数组）。
现规定：若想完成项目 groups[i][0]，必须先完成项目 groups[i][1]（即 groups[i][1] 是 groups[i][0] 的前置项目）。
已知所有分组均互不相同。若根据这些分组规则能顺利完成所有考核项目（即存在合法的完成顺序），请返回任意一个有效的完成顺序；若无法顺利完成（即存在循环依赖等情况），则返回空数组。


示例1
输入

```
3,[[2,1]]
```

输出

```
[1,2,0]

```

示例2
输入

```
3,[[1,0], [0,1]]
```

输出
[ ]
```
[1,2,0]

```

#### 思路分析


 - 🧠  **算法分析**：
   拓扑排序
   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/4bf04b0efb4b450c8e622f419155a744.png)


⚡ **代码实现**：

```cpp
// cpp版本
#include <vector>
class Solution {
public:
    vector<int> findOrder(int n, vector<vector<int> >& groups) {
        // write code here
        vector<vector<int> >edge(n);
        vector<int>in(n);
        for(auto&g:groups){
            edge[g[1]].push_back(g[0]);
            in[g[0]]++;
        }
        queue<int>q;
        for(int i = 0;i<n;i++){
            if(in[i]==0)q.push(i);
        }
        vector<int>result;
        while(!q.empty()){
            int t = q.front();
            q.pop();
            result.push_back(t);
            for(int&x:edge[t]){
                if(--in[x]==0)q.push(x);
            }
        }
        if(result.size() == n){
            return result;
        }
        else{
            return vector<int>();
        }
    }
};
```
---
#### 合唱队形
- **题目链接**：[合唱队形](https://www.nowcoder.com/practice/0045cd3e39634a66ada63c2adeb49234?tpId=230&tqId=39759&ru=/exam/oj)
- **难度**：⭐⭐⭐
- **标签**：`最长上升子序列`

#### 💡 题目描述
有 N 位同学站成一排，音乐老师需要请其中的 (N-K) 位同学出列，使得剩下的 K 位同学能排成 “合唱队形”。
合唱队形的定义如下：设剩下的 K 位同学从左到右依次编号为 1，2，…，K，他们的身高分别为 T₁，T₂，…，Tₖ。则这 K 位同学的身高需满足：T₁ <T₂ < ... < Tᵢ> Tᵢ₊₁ > ... > Tₖ₋₁ > Tₖ（其中 1≤i≤K，即身高先严格递增到第 i 位，再严格递减）。
你的任务是：已知所有 N 位同学的身高，计算最少需要几位同学出列（即求最小的 N-K），才能让剩下的同学排成合唱队形。


示例1
输入

```
8
186 186 150 200 160 130 197 220
```

输出

```
4
```

#### 思路分析



 - 🧠  **算法图解**：
   两个最长上升子序列

⚡ **代码实现**：

```cpp
// cpp版本
#include <iostream>
using namespace std;
const int N = 1010;
int n,a[N],f[N],g[N];

int main() {
    cin>>n;
    for(int i = 1;i<=n;i++)cin>>a[i];
    for(int i = 1;i<=n;i++){
        f[i] = 1;
        for(int j = 1;j<i;j++){
            if(a[j]<a[i])
                f[i] = max(f[i],f[j]+1);
        }
    }
    for(int i = n;i>=1;i--){
        g[i] = 1;
        for(int j = n;j>i;j--){
            if(a[j]<a[i])
                g[i] = max(g[i],g[j]+1);
        }
    }
    int ret = 0;
    for(int i = 1;i<=n;i++){
        ret = max(ret,f[i]+g[i]-1);
    }
    cout<<n-ret<<'\n';
    return 0;
}
```

---
