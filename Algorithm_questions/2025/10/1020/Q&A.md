| question                                                     | tag          |
| ------------------------------------------------------------ | ------------ |
| [简写单词](https://www.nowcoder.com/share/jump/8978549211760919017220) | 模拟         |
| [dd爱框框](https://ac.nowcoder.com/acm/problem/221681)       | 滑动窗口     |
| [除2！](https://ac.nowcoder.com/acm/problem/213140)          | 模拟         |
| [Fibonacci数列_牛客题霸_牛客网](https://www.nowcoder.com/practice/18ecd0ecf5ef4fe9ba3f17f8d00d2d66?tpId=122&tqId=33668&ru=/exam/oj) | 模拟、数学   |
| [单词搜索_牛客题霸_牛客网](https://www.nowcoder.com/practice/987f2981769048abaf6180ed63266bb2?tpId=196&tqId=39583&ru=/exam/oj) | DFS/BFS      |
| [杨辉三角_牛客题霸_牛客网](https://www.nowcoder.com/practice/e671c6a913d448318a49be87850adbcc?tpId=290&tqId=39928&ru=/exam/oj) | 二维动态规划 |



## 简写单词

```c++
#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s,result;
    while(cin>>s){
        result += toupper(s[0]);
    }
    cout<<result<<endl;
    return 0;
}
// 64 位输出请用 printf("%lld")
```



## dd爱框框

```c++
#include <iostream>
#include <climits>

using namespace std;

const int N = 10000000+10;
int n,x,a[N];

int main(){
    cin>>n>>x;
    for(int i = 1;i<=n;i++)cin>>a[i];
    long long sum = 0;
    int l=-1,len = INT_MAX;
    for(int left = 1,right=1;right<=n;right++){
        sum += a[right];
        while(sum>=x){
            if(right-left+1<len){
                l = left;
                len = right-left+1;
            }
            sum-=a[left++];
        }
    }
    cout<<l<<" "<<len+l-1<<endl;
    return 0;
}
```

## 除2！

- 使用堆来简单模拟一下即可

```c++
#include <iostream>
#include <queue>

using namespace std;
int n, k;

int main() {
    cin >> n >> k;
    long long sum = 0;
    // 大根堆
    priority_queue<int>pq;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x & 1)sum += x;
        else pq.emplace(x);
    }
    while (k && !pq.empty()) {
        int t = pq.top();
        pq.pop();
        t >>= 1;
        k--;
        if (t & 1)sum += t;
        else pq.emplace(t);
    }
    while (!pq.empty()) {
        sum += pq.top();
        pq.pop();
    }
    cout << sum << endl;
    return 0;
}
```

## Fibonacci

```c++
#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;
    int a = 0,b = 1,c = 1;
    while(n>c)
    {
        a=b;
        b=c;
        c=a+b;
    }
    cout<<min(c-n,n-b);
    
    return 0;
}
// 64 位输出请用 printf("%lld")
```

## 单词搜索

- 一道纯粹的搜索题

```c++
#include <vector>
class Solution {
    int n,m;
    int dx[4]{0,0,1,-1},dy[4]{1,-1,0,0};
    vector<vector<bool> >vis;
    int dfs(const vector<string>&board,int i,int j,const string& word,int idx){
        if(idx==word.size())return true;
        vis[i][j] = true;
        for(int k = 0;k<4;k++){
            int x = i+dx[k],y = j+dy[k];
            if(x>=0&&x<n&&y>=0&&y<m&&board[x][y]==word[idx]&&!vis[x][y]){
                if(dfs(board,x,y,word,idx+1))return true;
            }
        }
        vis[i][j] = false;
        return false;
    }
public:
    bool exist(vector<string>& board, string word) {
        n = board.size(),m=board[0].size();
        vis.resize(n,vector<bool>(m));
        for(int i = 0;i<n;i++){
            for(int j = 0;j<m;j++){
                if(board[i][j]==word[0]){
                    if(dfs(board,i,j,word,1))return true;
                }
            }
        }
        return false;
    }
};
```

## 杨辉三角

```c++
#include <iostream>
using namespace std;
const int N = 35;
int grid[N][N];

int main() {
    int n;
    cin>>n;
    for(int i = 1;i<=n;i++){
        grid[i][1] = grid[i][i] = 1;
    }
    for(int i = 3;i<=n;i++){
        for(int j = 2;j<i;j++){
            grid[i][j] = grid[i-1][j]+grid[i-1][j-1];
        }
    }
    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=i;j++){
            printf("%5d",grid[i][j]);
        }
        cout<<'\n';
    }
}
// 64 位输出请用 printf("%lld")
```

