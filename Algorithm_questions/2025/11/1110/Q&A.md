#### 天使果冻

- **题目链接**：[天使果冻](https://ac.nowcoder.com/acm/problem/219641)
- **难度**：⭐⭐
- **标签**：`第二大问题`

#### 💡 题目描述
有 n 个果冻排成一排，第 i 个果冻的美味度为 aᵢ。
天使非常喜欢吃果冻，但她想把最好吃的果冻留到最后收藏。现在有 q 次询问，每次询问会给出一个 x，需要回答前 x 个果冻中，美味度第二大的果冻的美味度是多少？
注：如果前 x 个果冻中最大的美味度出现两次及以上，那么第二大的美味度等同于最大的美味度。例如序列 [2, 3, 4, 2, 4] 中，最大美味度 4 出现了 2 次，因此第二大的美味度是 4。


示例1
输入

```
5
1 2 5 3 5
4
2
3
4
5
```

输出

```
1
2
3
5
```


#### 思路分析

 - 🧠  **算法分析**：
   

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/769f08183bb14a6299fb5ca9cc18d0ac.png)


2. ⚡ **代码实现**：

```cpp
// cpp版本
#include <iostream>
#include <climits>

using namespace std;
const int N = 1e5+10;
int n,a[N],q,f[N],g[N];

int main(){
    cin>>n;
    for(int i = 1;i<=n;i++)cin>>a[i];
    f[1] = a[1],g[1] = INT_MIN;
    for(int i = 2;i<=n;i++){
        f[i] = f[i-1];
        g[i] = g[i-1];
        if(a[i] >= f[i]){
            g[i] = f[i];
            f[i] = a[i];
        }
        else if(a[i]>g[i]){
            g[i] = a[i];
        }
    }
    cin>>q;
    while(q--){
        int x;
        cin>>x;
        cout<<g[x]<<endl;
    }
    return 0;
}
```

---
#### dd爱旋转

- **题目链接**：[dd爱旋转](https://ac.nowcoder.com/acm/problem/221786)
- **难度**：⭐⭐⭐
- **标签**：`找规律`

#### 💡 题目描述
读入一个 n×n 的矩阵，对该矩阵有以下两种操作：
操作 1：顺时针旋转 180°
操作 2：关于行镜像


示例1
输入

```
2
1 2
3 4
1
1
```

输出

```
4 3
2 1
```
示例2
输入

```
2
1 2
3 4
1
2
```

输出

```
3 4
1 2
```

#### 思路分析



 - 🧠  **算法分析**：
   

见代码

⚡ **代码实现**：

```cpp
// cpp版本
#include <iostream>

using namespace std;
const int N = 1010;
int n,g[N][N],q;
void SetRow(){
    for(int i = 1;i<=n/2;i++){
        for(int j = 1;j<=n;j++){
            swap(g[i][j],g[n-i+1][j]);
        }
    }
}
void SetCol(){
    for(int j = 1;j<=n/2;j++){
        for(int i = 1;i<=n;i++){
            swap(g[i][j],g[i][n-j+1]);
        }
    }
}

int main(){
    cin>>n;
    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=n;j++)cin>>g[i][j];
    }
    cin>>q;
    int row = 0,col = 0;
    while(q--){
        int x;
        cin>>x;
        // 顺时针旋转180，相当于一次行对称+一次列对称
        if(x==1)row++,col++;
        else row++;
    }
    row%=2,col%=2;
    if(row)SetRow();
    if(col)SetCol();
    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=n;j++){
            cout<<g[i][j]<<' ';
        }
        cout<<'\n';
    }
    return 0;
}
```
---
#### 小红取数
- **题目链接**：[小红取数]()
- **难度**：⭐⭐⭐
- **标签**：`01背包`，同余定理

#### 💡 题目描述
小红拿到了一个数组，她想取一些数使得取的数之和尽可能大，但要求这个和必须是 
k的倍数。你能帮帮她吗？


示例1
输入

```
5 5
4 8 2 9 1
```

输出

```
20
```

#### 思路分析



 - 🧠  **算法图解**：
   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e8ec1a35abf54e6c859d0e2805fd9acc.png)


⚡ **代码实现**：

```cpp
// cpp版本

#include <climits>
#include <cstring>
#include <iostream>

using namespace std;
typedef long long LL;
int getmod(LL a, int b) {
    return (a % b + b) % b;
}
const int N = 1010;
int n, k;
LL a[N], dp[N][N];

int main() {
    cin >> n >> k;
    for (int i = 1; i <= n; i++)cin >> a[i];
    memset(dp, -0x3f, sizeof dp);
    dp[0][0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < k; j++) {
            // 不选
            dp[i][j] = dp[i - 1][j];
            // 选
            dp[i][j] = max(dp[i][j], dp[i - 1][getmod(j - a[i], k)] + a[i]);
        }
    }
    if (dp[n][0] <= 0)cout << -1 << endl;
    else cout << dp[n][0] << endl;
    return 0;

```

---
