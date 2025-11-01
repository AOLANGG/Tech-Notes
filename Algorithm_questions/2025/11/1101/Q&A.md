| question                                                     | tag      |
| ------------------------------------------------------------ | -------- |
| [kotori和气球](https://ac.nowcoder.com/acm/problem/50039)    | 排列组合 |
| [ **走迷宫**](https://www.nowcoder.com/practice/e88b41dc6e764b2893bc4221777ffe64?tpId=308&tqId=40477&ru=/exam/oj) | BFS      |
| [**主持人调度（二）**](https://www.nowcoder.com/practice/4edf6e6d01554870a12f218c94e8a299?tpId=196&tqId=37562&ru=/exam/oj) | 堆       |
| [游游的重组偶数](https://www.nowcoder.com/questionTerminal/d1ac7f15d5dc40b39a7d6cb11a01407e) | 模拟     |
| [体操队形](https://ac.nowcoder.com/acm/problem/229386)       | DFS      |
| [二叉树中的最大路径和](https://www.nowcoder.com/practice/da785ea0f64b442488c125b441a4ba4a?tpId=196&tqId=37050&ru=/exam/oj) | 二叉树   |

## kotori和气球

```c++
#include <iostream>

using namespace std;

int main(){
    int n,m;
    cin>>n>>m;
    int ret = n;
    for(int i = 0;i<m-1;i++)ret = (ret*(n-1))%109;
    cout<<ret<<endl;
    return 0;
}
```

## **走迷宫**

```c++
#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int n, m, x1, y1, x2, y2;
const int N = 1010;
char s[N][N];
bool vis[N][N];
int dx[4] {1, -1, 0, 0}, dy[4] {0, 0, 1, -1};

int bfs() {
    queue<pair<int, int> >q;
    q.push({x1, y1});
    vis[x1][y1] = true;
    int cnt = 0;
    while (!q.empty()) {
        int sz = q.size();
        cnt++;
        for (int i = 0; i < sz; i++) {
            auto t = q.front();
            q.pop();
            for (int k = 0; k < 4; k++) {
                int x = t.first + dx[k], y = t.second + dy[k];
                if (x >= 1 && x <= n && y >= 1 && y <= m && s[x][y] == '.' && !vis[x][y]) {
                    if (x == x2 && y == y2) {
                        return cnt;
                    }
                    vis[x][y] = true;
                    q.push({x,y});
                }
            }
        }
    }
    return -1;
}
int main() {
    cin >> n >> m >> x1 >> y1 >> x2 >> y2;
    for (int i = 1; i <= n; i++)
        scanf("%s", s[i] + 1);
    cout << bfs() << endl;
    return 0;
}
```

## **主持人调度（二）**

```c++
#include <queue>
class Solution {
public:
    int minmumNumberOfHost(int n, vector<vector<int> >& startEnd) {
        sort(startEnd.begin(),startEnd.end());
        // 定义一个小根堆
        priority_queue<int,vector<int>,greater<int> >pq;
        pq.push(startEnd[0][1]);
        for(int i = 1;i<n;i++){
            int t = pq.top();
            if(t<=startEnd[i][0]){
                pq.pop();
                
            }
            pq.push(startEnd[i][1]);
        }
        return pq.size();
    }
};
```

## 游游的重组偶数

```c++
#include <iostream>
#include <string>

using namespace std;


int main(){
    int q;
    cin>>q;
    while(q--){
        string s;
        cin>>s;
        int n = s.size(),idx = -1;
        for(int i = 0;i<n;i++){
            if((s[i]-'0')%2==0){
                idx = i;
                break;
            }
        }
        if(idx!=-1){
            if(s[n-1]!='0')
                swap(s[idx],s[n-1]);
            cout<<s<<endl;
        }
        else cout<<-1<<endl;
    }
}
```

## 体操队形

```c++
#include <iostream>

using namespace std;
const int N = 15;
int n;
bool vis[N];
int arr[N];
int ret;

void dfs(int pos){
    if(pos==n+1){
        ret++;
        return;
    }
    for(int i = 1;i<=n;i++){
        if(vis[i])continue;
        if(vis[arr[i]])return;
        vis[i] = true;
        dfs(pos+1);
        vis[i] = false;
    }
}
int main(){
    cin>>n;
    for(int i = 1;i<=n;i++)cin>>arr[i];
    dfs(1);
    cout<<ret<<endl;
    return 0;
}
```

## **二叉树中的最大路径和**

```c++
class Solution {
    int ret = INT_MIN;
    int getVal(TreeNode* node){
        if(node==nullptr)return 0;
        int leftVal = max(0,getVal(node->left));
        int rightVal =max(0, getVal(node->right));
        ret = max(ret,leftVal+rightVal+node->val);
        return max(leftVal,rightVal)+node->val;
    }
public:
    int maxPathSum(TreeNode* root) {
        // write code here
        getVal(root);
        return ret;
    }
};
```

