| question                                                     | tag          |
| ------------------------------------------------------------ | ------------ |
| [字符串中找出连续最长的数字串_牛客题霸_牛客网](https://www.nowcoder.com/practice/bd891093881d4ddf9e56e7cc8416562d?tpId=182&tqId=34785&ru=/exam/oj) | 模拟         |
| [岛屿数量_牛客题霸_牛客网](https://www.nowcoder.com/practice/0c9664d1554e466aa107d899418e814e?tpId=196&tqId=37167&ru=/exam/oj) | DFS          |
| [拼三角](https://ac.nowcoder.com/acm/problem/219046)         | 暴力枚举     |
| [求最小公倍数_牛客题霸_牛客网](https://www.nowcoder.com/practice/22948c2cad484e0291350abad86136c3?tpId=37&tqId=21331&ru=/exam/oj) | 基础数学     |
| [字母收集_牛客题霸_牛客网](https://www.nowcoder.com/practice/9740ce2df0a04399a5ade1927d34c1e1?tpId=230&tqId=38954&ru=/exam/oj) | 二维动态规划 |
| [数组中的最长连续子序列_牛客题霸_牛客网](https://www.nowcoder.com/practice/eac1c953170243338f941959146ac4bf?tpId=196&tqId=37143&ru=/exam/oj) | 排序、双指针 |



## [字符串中找出连续最长的数字串_牛客题霸_牛客网](https://www.nowcoder.com/practice/bd891093881d4ddf9e56e7cc8416562d?tpId=182&tqId=34785&ru=/exam/oj)

```c++
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin>>s;
    int l=-1,r=0,n = s.size();
    int b=0,len = 1;
    while(r<n){
        if(s[r]>='0'&&s[r]<='9'){
            l = r;
            while(r<n&&s[r]>='0'&&s[r]<='9')r++;
            if(r-l>len){
                b = l;
                len = r-l;
            }
        }
        r++;
    }
    cout<<s.substr(b,len)<<endl;
    return 0;
}
// 64 位输出请用 printf("%lld")
```



## [岛屿数量_牛客题霸_牛客网](https://www.nowcoder.com/practice/0c9664d1554e466aa107d899418e814e?tpId=196&tqId=37167&ru=/exam/oj)

```c++
#include <functional>
class Solution {
    int n,m;
    vector<vector<bool> >vis;
    int dx[4]{1,-1,0,0},dy[4]{0,0,1,-1};
    void dfs(int i,int j,const vector<vector<char> >&grid){
        vis[i][j]=true;
        for(int k = 0;k<4;k++){
            int x = i+dx[k],y = j+dy[k];
            if(x>=0&&x<n&&y>=0&&y<m&&grid[x][y]=='1'&&!vis[x][y]){
                dfs(x,y,grid);
            }
        }
    }
public:
    int solve(vector<vector<char> >& grid) {
        // write code here
        n = grid.size(),m = grid[0].size();
        vis.resize(n,vector<bool>(m));
        int ret = 0;
        for(int i = 0;i<n;i++){
            for(int j = 0;j<m;j++){
                if(grid[i][j]=='1'&&!vis[i][j]){
                    ret++;
                    dfs(i,j,grid);
                }
            }
        }
        return ret;
    }
};
```

## [拼三角](https://ac.nowcoder.com/acm/problem/219046)

```c++
#include <iostream>
#include <algorithm>

using namespace std;
const int N = 10;
int arr[N];

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        for(int i = 0;i<6;++i)
            cin>>arr[i];
        sort(arr,arr+6);
        if(arr[0] + arr[1] > arr[2] && arr[3] + arr[4] > arr[5] ||
         arr[0] + arr[2] > arr[3] && arr[1] + arr[4] > arr[5] ||
         arr[0] + arr[3] > arr[4] && arr[1] + arr[2] > arr[5] ||
         arr[0] + arr[4] > arr[5] && arr[1] + arr[2] > arr[3])
            cout << "Yes" << endl;
        else cout<<"No"<<endl;
    }
    return 0;
}
```

## [求最小公倍数_牛客题霸_牛客网](https://www.nowcoder.com/practice/22948c2cad484e0291350abad86136c3?tpId=37&tqId=21331&ru=/exam/oj)

```c++
#include <iostream>
using namespace std;
int gcd(int a,int b){
    if(b==0)return a;
    return gcd(b,a%b);
}
int lcm(int a,int b){
    return a/gcd(a,b)*b;
}
int main() {
    int a,b;
    cin>>a>>b;
    cout<<lcm(a,b)<<endl;
    return 0;
}
// 64 位输出请用 printf("%lld")
```

## [字母收集_牛客题霸_牛客网](https://www.nowcoder.com/practice/9740ce2df0a04399a5ade1927d34c1e1?tpId=230&tqId=38954&ru=/exam/oj)

```c++
#include <iostream>
#include <vector>

using namespace std;
int count(char ch) {
    if (ch == 'l')return 4;
    else if (ch == 'o')return 3;
    else if (ch == 'v')return 2;
    else if (ch == 'e')return 1;
    return 0;
}
int main() {
    int n, m;
    cin >> n >> m;
    vector<string>grid(n);
    for (int i = 0; i < n; i++)cin >> grid[i];
    vector<vector<int> >f(n, vector<int>(m));
    // f[i][j] = max(f[i-1][j],f[i][j-1])+count(grid[i][j]);
    f[0][0] = count(grid[0][0]);
    for (int j = 1; j < m; ++j) {
        f[0][j] = f[0][j - 1] + count(grid[0][j]);
    }
    for (int i = 1; i < n; ++i) {
        f[i][0] = f[i - 1][0] + count(grid[i][0]);
    }

    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            f[i][j] = max(f[i - 1][j], f[i][j - 1]) + count(grid[i][j]);
        }
    }
    cout << f[n - 1][m - 1] << endl;
    return 0;
}
// 64 位输出请用 printf("%lld")
```

## [数组中的最长连续子序列_牛客题霸_牛客网](https://www.nowcoder.com/practice/eac1c953170243338f941959146ac4bf?tpId=196&tqId=37143&ru=/exam/oj)

```c++
class Solution {
public:
    int MLS(vector<int>& arr) {
        sort(arr.begin(),arr.end());
        int ret = 1;
        int n = arr.size();
        for(int i = 0;i<n;){
            int j = i+1,count = 1;
            while(j<n){
                if(arr[j]==arr[j-1]+1){
                    j++,count++;
                }else if(arr[j]==arr[j-1]){
                    j++;
                }else{
                    break;
                }
            }
            ret = max(ret,count);
            i = j;
        }
        return ret;
    }
};
```

