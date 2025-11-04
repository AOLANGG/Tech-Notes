#### 素数回文

- **题目链接**：[素数回文](https://www.nowcoder.com/practice/d638855898fb4d22bc0ae9314fed956f?tpId=290&tqId=39945&ru=/exam/oj)
- **难度**：⭐
- **标签**：`模拟`、`数学`

#### 💡 题目描述

现在给出一个素数，这个素数满足两点：

1、  只由1-9组成，并且每个数只出现一次，如13,23,1289。

2、  位数从高到低为递减或递增，如2459，87631。

请你判断一下，这个素数的回文数是否为素数（13的回文数是131,127的回文数是12721）。

示例1
输入

```
13
```

输出

```
prime
```
示例2
输入

```
17
```

输出

```
noprime
```

#### 思路分析

如果t的回文数仍是素数，则输出“prime”，否则输出"noprime"。

 - 🧠  **算法分析**：
   
- 模拟生成题中要求的回文串
- 将这个回文串转换成`long long`类型的整数
- 判断这个整数是否是质数即可


2. ⚡ **代码实现**：

```cpp
// cpp版本
#include <iostream>
#include <cmath>
#include <string>
#include <cstdlib>

using namespace std;
bool isPrime(long long x){
    for(long long i = 2;i<=sqrt(x);i++){
        if(x%i==0)return false;
    }
    return x>=2;
}
int main() {
    string s;
    cin>>s;
    int n = s.size();
    for(int i = n-2;i>=0;i--)s+=s[i];
    // cout<<s<<endl;
    if(isPrime(atol(s.c_str())))cout<<"prime"<<endl;
    else cout<<"noprime"<<endl;
    return 0;
}
```

---
#### 活动安排

- **题目链接**：[活动安排](https://www.nowcoder.com/practice/16d971e9e42e4f3b9b1e2b8794796a43?tpId=308&tqId=40488&ru=/exam/oj)
- **难度**：⭐⭐⭐
- **标签**：`排序`、`贪心`

#### 💡 题目描述

给定 n 个活动，每个活动的时间区间为 [a_i, b_i)（左闭右开，即活动在 a_i 开始，b_i 结束，b_i 时刻活动已结束）。要求选择最多的活动，使得选中的活动时间两两不重合。

示例1
输入

```
3
1 4
1 3
3 5
```

输出

```
2
```

#### 思路分析

输出一行一个整数，表示最多可选择的活动数。

 - 🧠  **算法分析**：
   
1. 排序活动：将所有活动按照结束时间 b_i 从小到大排序。
2. 贪心选择：从排序后的活动中，依次选择与上一个选中活动不重叠的活动（即当前活动的开始时间 a_i 大于等于上一个活动的结束时间）。

⚡ **代码实现**：

```cpp
// cpp版本
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin>>n;
    vector<pair<int,int> >event(n);
    for(int i = 0;i<n;i++){
        cin>>event[i].first>>event[i].second;
    }
    sort(event.begin(),event.end());
    int ret = 1;
    int e = event[0].second;
    // 选择重复区间的最小右端点
    for(int i = 1;i<n;i++){
        if(e>event[i].first){
            e = min(e,event[i].second);
        }
        else {
            ret++;
            e = event[i].second;
        }
    }
    cout<<ret<<endl;
    return 0;
}
```
---
#### 合唱团

- **题目链接**：[合唱团](https://www.nowcoder.com/practice/661c49118ca241909add3a11c96408c8?tpId=122&tqId=33652&ru=/exam/oj)
- **难度**：⭐⭐⭐⭐
- **标签**：`动态规划`

#### 💡 题目描述

小红拿到了一个正整数 x。她可以将 x 的部分数位染成红色，剩余数位保持未染色状态。
她希望所有染红的数位对应的数字之和，与未染色的数位对应的数字之和相等。请判断是否能达成这个目标。

示例1
输入

```
3
7 4 7
2 50
```

输出

```
49
```

#### 思路分析

从数组中挑选一些数出来，相对顺序不变，求最长严格递增子序列的长度

 - 🧠  **算法图解**：
   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/a1868f5b326c4a02996f893d346d55d8.png#pic_center)
   如图

⚡ **代码实现**：

```cpp
// cpp版本
#include <iostream>
using namespace std;
typedef long long LL;
const int N = 55, M = 15;
const LL INF = 0x3f3f3f3f3f3f3f3f;
int n, k, d;
LL arr[N];
LL f[N][M], g[N][M];
int main()
{
	cin >> n;
	for (int i = 1; i <= n; i++) cin >> arr[i];
	cin >> k >> d;
	// 初始化放在填表中进⾏了
	for (int i = 1; i <= n; i++) // 填写每⼀⾏
	{
		g[i][1] = f[i][1] = arr[i];
		for (int j = 2; j <= min(i, k); j++) // 挑选⼏个⼈
		{
			f[i][j] = -INF; // 初始化
			g[i][j] = INF; // 初始化
			for (int prev = max(i - d, j - 1); prev <= i - 1; prev++) // 前⾯挑选的最后⼀个位置
			{
			f[i][j] = max(max(f[prev][j - 1] * arr[i], g[prev][j - 1] *
		   arr[i]), f[i][j]);
			g[i][j] = min(min(f[prev][j - 1] * arr[i], g[prev][j - 1] *
		   arr[i]), g[i][j]);
			}
		}
	}
	LL ret = -INF;
	for (int i = k; i <= n; i++) ret = max(ret, f[i][k]);
	cout << ret << endl;
	return 0;
}
```

---
