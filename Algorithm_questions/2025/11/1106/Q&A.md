#### ISBN号码

- **题目链接**：[ISBN号码](https://www.nowcoder.com/practice/95712f695f27434b9703394c98b78ee5?tpId=290&tqId=39864&ru=/exam/oj)
- **难度**：⭐⭐
- **标签**：`模拟`

#### 💡 题目描述
每一本正式出版的图书都有一个ISBN号码与之对应，ISBN码包括9位数字、1位识别码和3位分隔符，其规定格式如“x-xxx-xxxxx-x”，其中符号“-”是分隔符（键盘上的减号），最后一位是识别码，例如0-670-82162-4就是一个标准的ISBN码。ISBN码的首位数字表示书籍的出版语言，例如0代表英语；第一个分隔符“-”之后的三位数字代表出版社，例如670代表维京出版社；第二个分隔之后的五位数字代表该书在出版社的编号；最后一位为识别码。
识别码的计算方法如下：
首位数字乘以1加上次位数字乘以2……以此类推，用所得的结果mod 11，所得的余数即为识别码，如果余数为10，则识别码为大写字母X。例如ISBN号码0-670-82162-4中的识别码4是这样得到的：对067082162这9个数字，从左至右，分别乘以1，2，…，9，再求和，即0×1+6×2+……+2×9=158，然后取158 mod 11的结果4作为识别码。
你的任务是编写程序判断输入的ISBN号码中识别码是否正确，如果正确，则仅输出“Right”；如果错误，则输出你认为是正确的ISBN号码。


示例1
输入

```
0-670-82162-4
```

输出

```
Right
```
示例2
输入

```
0-670-82162-0
```

输出

```
0-670-82162-4
```

#### 思路分析
判断是否是正确的ISBN号码，不是的话，要输出正确的ISBN号码

 - 🧠  **算法分析**：
   
- 按照题目要求，进行模拟，得出来的结果对11取模，考虑10这个特殊情况
  - 如果是10，就要和'X'比较
  - 否则和对应的字符比较


2. ⚡ **代码实现**：

```cpp
// cpp版本
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin>>s;
    int n = s.size(),num = 1,ret = 0;
    for(int i = 0;i<n-1;i++){
        if(s[i]>='0'&&s[i]<='9'){
            ret += (s[i]-'0')*num;
            num++;
        }
    }
    ret%=11;
    if(ret==10){
        if(s[n-1]=='X')cout<<"Right"<<endl;
        else{
            s[n-1]='X';
            cout<<s<<endl;
        }
    }
    else{
        if(s[n-1]==ret+'0')cout<<"Right"<<endl;
        else {
            s[n-1] = ret+'0';
            cout<<s<<endl;
        }
    }
    return 0;
}
// 64 位输出请用 printf("%lld")
```

---
#### kotori和迷宫

- **题目链接**：[kotori和迷宫]()
- **难度**：⭐⭐
- **标签**：`BFS`

#### 💡 题目描述

kotori在一个n*m迷宫里，迷宫的最外层被岩浆淹没，无法涉足，迷宫内有k个出口。kotori只能上下左右四个方向移动。她想知道有多少出口是她能到达的，最近的出口离她有多远？

示例1
输入

```
6 8
e.*.*e.*
.**.*.*e
..*k**..
***.*.e*
.**.*.**
*......e
```

输出

```
2 7
```


#### 思路分析

有多少出口是她能到达的，最近的出口离她有多远

 - 🧠  **算法分析**：
   从起点开始，对整个矩阵进行BFS搜索


⚡ **代码实现**：

```cpp
// cpp版本
#include <iostream>
#include <queue>
#include <cstring>
#include <climits>

using namespace std;
int x1,y1;// 标记起点位置
int n,m;
const int N = 35;
char arr[N][N];
int dist[N][N];
queue<pair<int,int> >q;

int dx[4]{1,-1,0,0},dy[4]{0,0,1,-1};

void bfs(){
    // 两层含义 
    // 1.当前位置是否搜索过
    // 2. 最小的距离
    memset(dist,-1,sizeof dist);
    dist[x1][y1] = 0;
    q.emplace(x1,y1);
    while(!q.empty()){
        auto t = q.front();
        q.pop();
        for(int k = 0;k<4;k++){
            int x = t.first+dx[k],y = t.second+dy[k];
            if(x>=0&&x<n&&y>=0&&y<m&&arr[x][y]!='*'&&dist[x][y]==-1){
                dist[x][y] = dist[t.first][t.second] + 1;
                if(arr[x][y]!='e')q.emplace(x,y);
            }
        }
    }
}
int main(){
    cin>>n>>m;
    for(int i = 0;i<n;i++)scanf("%s",arr[i]);
    for(int i=0;i<n;i++){
        for(int j = 0;j<m;j++){
            if(arr[i][j] == 'k')x1 = i,y1 = j;
        }
    }    
    bfs();
    int count = 0,ret = INT_MAX;
    for(int i = 0;i<n;i++){
        for(int j = 0;j<m;j++){
            if(arr[i][j]=='e' && dist[i][j]!=-1){
                count++;
                ret = min(ret,dist[i][j]);
            }
        }
    }
    if(count==0)cout<<-1<<endl;
    else cout<<count<<" "<<ret<<endl;
    return 0;
}
```
---
####  矩阵最长递增路径
- **题目链接**：[ 矩阵最长递增路径](https://www.nowcoder.com/practice/7a71a88cdf294ce6bdf54c899be967a2?tpId=196&tqId=37184&ru=/exam/oj)
- **难度**：⭐⭐
- **标签**：`搜索`

#### 💡 题目描述
给定一个 n 行 m 列的矩阵 matrix，矩阵内所有元素均为非负整数。你需要在矩阵中找到一条最长路径，使得这条路径上的元素是严格递增的，并输出这条最长路径的长度。
这条路径必须满足以下条件：
对于每个单元格，只能向上下左右四个方向移动，不能沿对角线方向移动，也不能移动到矩阵边界外。
路径不能包含重复的单元格，即每个格子最多只能经过一次。
数据范围：1 ≤ n, m ≤ 10000 ≤ matrix [i][j] ≤ 1000
进阶要求：空间复杂度 O (nm)，时间复杂度 O (nm)
例如：当输入矩阵为 [[1,2,3],[4,5,6],[7,8,9]] 时，对应的输出为 5
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/914cbf19f4404fbf80c805ae935c60e2.png)


示例1
输入

```
[[1,2,3],[4,5,6],[7,8,9]]
```

输出

```
5
```
示例2
输入

```
[[1,2],[4,3]]
```

输出

```
4
```
#### 思路分析
最长递增子序列的长度

 - 🧠  **算法图解**：
   每个位置都保存搜索的结果，这样再次遍历这个位置的时候就可以直接使用它

⚡ **代码实现**：

```cpp
// cpp版本
class Solution {
    int n,m;
    int dx[4]{0,0,1,-1},dy[4]{1,-1,0,0};
    int memo[1010][1010];
    int dfs(const vector<vector<int> >&matrix,int i,int j){
        if(memo[i][j]!=-1)return memo[i][j];
        int len = 1;
        for(int k = 0;k<4;k++){
            int x = i+dx[k],y = j+dy[k];
            if(x>=0&&x<n&&y>=0&&y<m&&matrix[x][y] > matrix[i][j]){
                len = max(len,1+dfs(matrix,x,y));
            }
        }
        return memo[i][j] = len;
    }
public:
    int solve(vector<vector<int> >& matrix) {
        memset(memo,-1,sizeof memo);
        n = matrix.size(),m =matrix[0].size();
        int ret = 1;
        for(int i = 0;i<n;i++){
            for(int j = 0;j<m;j++){
                ret = max(ret,dfs(matrix,i,j));
            }
        }
        return ret;
    }
};
```

---
