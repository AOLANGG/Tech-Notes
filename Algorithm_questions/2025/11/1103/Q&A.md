#### 小红的口罩

- **题目链接**：[小红的口罩](https://ac.nowcoder.com/acm/problem/229953)
- **难度**：⭐⭐
- **标签**：`贪心`、`堆`

#### 💡 题目描述

疫情来了，小红网购了 n 个口罩。戴口罩会有不舒适度，每个口罩戴一天的初始不舒适度为 a_i。
小红会重复使用口罩（不卫生，仅题目设定），每次重复使用时，该口罩的不舒适度会翻倍。
小红想知道，在不舒适度总和不超过 k 的情况下，最多能用现有的口罩度过多少天？

第一行输入两个正整数 n 和 k，分别代表口罩的总数、小红最多能忍受的不舒适度总和。第二行输入 n 个正整数 a_i（用空格隔开），代表每个口罩初始的不舒适度。数据范围：1≤n≤10^5，1≤a_i、k≤10^9。

示例1
输入

```
2 30
2 3
```

输出

```
5
```
示例2
输入

```
3 5
7 6 8
```

输出

```
0
```

#### 思路分析

在不舒适度总和不超过 k 的情况下，最多能用现有的口罩度过多少天？

 - 🧠  **算法分析**：
   

使用小根堆，每次挑选出不舒适度最小的元素来考虑

- 计算总不舒适度，和给出的`k`进行大小判断即可


2. ⚡ **代码实现**：

```cpp
// cpp版本
//CSDN：https://blog.csdn.net/2301_79420799?type=blog
#include <iostream>
#include <queue>
#include <vector>

using namespace std;
int n, k;

int main() {
    cin >> n >> k;
    int ret = 0;
    long long sum = 0;
    // 小根堆
    priority_queue<int, vector<int>, greater<int> >pq;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        pq.emplace(x);
    }
    while (sum <= k) {
        int t = pq.top();
        pq.pop();
        sum += t;
        ret++;
        pq.emplace(t << 1);
    }
    cout << ret - 1 << endl;

    return 0;
}
```

---
#### 春游

- **题目链接**：[春游](https://ac.nowcoder.com/acm/problem/219035)
- **难度**：⭐⭐⭐
- **标签**：`贪心`、`数学`

#### 💡 题目描述

盼望着，盼望着，东风来了，春天脚步近了。值此大好春光，老师组织了同学们出去划船，划船项目收费规则如下：
双人船：最多坐两人，也可坐一人，收费 a 元。
三人船：最多坐三人，也可坐两人或一人，收费 b 元。
本次出游加上带队老师共 n 人，如何安排船只才能使得花费最小？

示例1
输入

```
2
2 20 200
3 20 20
```

输出

```
20
20
```

#### 思路分析

如何安排船只才能使得花费最小？

 - 🧠  **算法分析**：
   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/a1c68bd3e9dd49ed86d501417b013410.png#pic_center)
   考虑`3a`和`2b`的大小关系，分析出租哪个船平均一个人花费最少

- 最后有剩余的人的时候，需要考虑是否需要和最后一组进行搭配


2. ⚡ **代码实现**：

```cpp
// cpp版本
#include <iostream>

using namespace std;
typedef long long LL;
LL t,n,a,b;
LL func(){
    if(n<=2)return min(a,b);
    LL ret = 0;
    if(a*3<b*2){
        // 尽可能选择双人
        ret += n/2*a;
        n%=2;
        if(n){
            ret += min(a,b-a);
        }
    }
    else{
        // 尽可能选择三人
        ret += n/3*b;
        n%=3;
        if(n==1){
            ret += min(min(a,b),2*a-b);
        }
        else if(n==2){
            ret += min(min(a,b),3*a-b);
        }
    }
    return ret;
}
int main(){
    cin>>t;
    while(t--){
        cin>>n>>a>>b;
        cout<<func()<<endl;
    }
    return 0;
}
```
---
#### 数位染色

- **题目链接**：[数位染色](https://www.nowcoder.com/practice/adf828f399de4932955734a4eac12757?tpId=230&tqId=38956&ru=/exam/oj)
- **难度**：⭐⭐
- **标签**：`01背包`

#### 💡 题目描述

小红拿到了一个正整数 x。她可以将 x 的部分数位染成红色，剩余数位保持未染色状态。
她希望所有染红的数位对应的数字之和，与未染色的数位对应的数字之和相等。请判断是否能达成这个目标。

示例1
输入

```
1234567
```

输出

```
Yes
```
示例2
输入

```
23
```

输出

```
No
```

#### 思路分析

从数组中挑选一些数出来，相对顺序不变，求最长严格递增子序列的长度

 - 🧠  **算法图解**：
   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b53990bb65c540f19ea9216bf6107df1.png#pic_center)

参考图片


2. ⚡ **代码实现**：

```cpp
// cpp版本
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    string s;
    cin>>s;
    int n = s.size();
    int sum = 0;
    for(const char&ch:s)
        sum += ch-'0';
    if(sum%2){
        cout<<"No"<<endl;
    }
    else{
        int target = sum/2;
        vector<vector<bool>>f(n+1,vector<bool>(target+1));
        f[0][0] = true;
        //f[i][j]表示是否存在 从前i个字符中挑选，总和为j
        // f[i][j] = f[i-1][j];
        // f[i][j] = f[i-1][j-s[i-1]+'0']
        for(int i = 1;i<=n;i++){
            for(int j = 0;j<=target;j++){
                f[i][j] = f[i-1][j];
                if(j>=s[i-1]-'0')f[i][j] = f[i][j]||f[i-1][j-s[i-1]+'0'];
            }
        }
        if(f[n][target])cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }

    return 0;
}
```
---
3. 💭  **复杂度分析**：
   - **时间复杂度**：O(N*2)
   - **空间复杂度**：O(N*2)，用了数组`f`来存储`dp`表

---
