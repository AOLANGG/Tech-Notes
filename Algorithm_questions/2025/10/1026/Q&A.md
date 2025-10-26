| question                                                     | tag            |
| ------------------------------------------------------------ | -------------- |
| [平方数](https://ac.nowcoder.com/acm/problem/205350)         | 数学           |
| [分组](https://ac.nowcoder.com/acm/problem/229023)           | 枚举结果、二分 |
| [【模板】拓扑排序_牛客题霸_牛客网](https://www.nowcoder.com/practice/88f7e156ca7d43a1a535f619cd3f495c?tpId=308&tqId=40470&ru=/exam/oj) | 拓扑排序       |
| [字符串替换_牛客题霸_牛客网](https://www.nowcoder.com/practice/f094aed769d84cf3b799033c82fc1bf6?tpId=182&tqId=34710&ru=/exam/oj) | 模拟           |
| [神奇数_牛客笔试题_牛客网](https://www.nowcoder.com/questionTerminal/99fa7be28d5f4a9d9aa3c98a6a5b559a) | 模拟           |
| [DNA序列_牛客题霸_牛客网](https://www.nowcoder.com/practice/e8480ed7501640709354db1cc4ffd42a?tpId=37&tqId=21286&ru=/exam/oj) | 滑动窗口       |

## [平方数](https://ac.nowcoder.com/acm/problem/205350)

```c++
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    long long n;
    cin>>n;
    long long x = sqrt(n);
    long long a = x*x,b = (x+1)*(x+1);
    cout<<(n-a<b-n?a:b)<<endl;
    return 0;
}
```

## [分组](https://ac.nowcoder.com/acm/problem/229023)



暴力解法

```c++
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main(){
    int n,m;
    cin>>n>>m;
    vector<int>a(n);
    unordered_map<int,int>hashMap;
    int maxVal = 0;
    for(int&x:a){
        cin>>x;
        maxVal = max(maxVal,++hashMap[x]);
    }
    for(int x = 1;x<=maxVal;x++){
        int g = 0;
        for(auto it = hashMap.begin();it!=hashMap.end();it++){
            g += it->second/x + (it->second%x==0?0:1);
        }
        if(g<=m){
            cout<<x<<endl;
            return 0;
        }
    }
    cout<<-1<<endl;
    return 0;
}
```

二分做法

```c++
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;
int n,m;
unordered_map<int,int>hashMap;

bool check(int x){
    int g = 0;
    for(auto it = hashMap.begin();it!=hashMap.end();it++){
        g += it->second/x + (it->second%x==0?0:1);
    }
    return g<=m;
}
int main(){
    
    cin>>n>>m;
    vector<int>a(n);
    
    int maxVal = 0;
    for(int&x:a){
        cin>>x;
        maxVal = max(maxVal,++hashMap[x]);
    }
    int kinds = hashMap.size();
    if(kinds>m)cout<<-1<<endl;
    else{
        int l=1,r=maxVal;
        while(l<r){
            int mid = l+(r-l)/2;
            if(check(mid))r=mid;
            else l = mid+1;
        }
        cout<<l<<endl;
    }
    
    return 0;
}
```

## [【模板】拓扑排序_牛客题霸_牛客网](https://www.nowcoder.com/practice/88f7e156ca7d43a1a535f619cd3f495c?tpId=308&tqId=40470&ru=/exam/oj)

```c++
#include <iostream>
#include <queue>
#include <vector>
#include <unordered_map>

using namespace std;
int n,m;

int main() {
    cin>>n>>m;
    vector<vector<int> >edges(n+1);
    vector<int>in(n+1);
    for(int i = 0;i<m;i++){
        int u,v;
        cin>>u>>v;
        edges[u].emplace_back(v);
        in[v]++;
    }
    queue<int>q;
    for(int i = 1;i<=n;i++)
        if(in[i]==0)
            q.emplace(i);
    vector<int>ret;
    while(!q.empty()){
        int t = q.front();
        q.pop();
        ret.emplace_back(t);
        for(auto x:edges[t])
            if(--in[x]==0)
                q.emplace(x);
    }
    if (ret.size() == n) {
        for (int i = 0; i < n - 1; i++) {
            cout << ret[i] << " ";
        }
        cout << ret[n - 1]; // 测评会考虑最后⼀个元素的空格
    } else {
        cout << -1 << endl;
    }
    return 0;
}
// 64 位输出请用 printf("%lld")
```

## [字符串替换_牛客题霸_牛客网](https://www.nowcoder.com/practice/f094aed769d84cf3b799033c82fc1bf6?tpId=182&tqId=34710&ru=/exam/oj)

```c++
class StringFormat {
public:
    string formatString(string a, int n, vector<char> arg, int m) {
        // write code here
        string ret;
        int idx = 0;
        for (int i = 0; i < n; i++) {
            if (a[i] == '%') {
                i++;
                ret += arg[idx++];
            }
            else ret += a[i];
        }
        while(idx<m) ret += arg[idx++];
        return ret;
    }
};
```



## [神奇数_牛客笔试题_牛客网](https://www.nowcoder.com/questionTerminal/99fa7be28d5f4a9d9aa3c98a6a5b559a)

```c++
#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;
int nums[10];

bool isPrime(int n){
    if(n<2)return false;
    for(int i = 2;i<=sqrt(n);i++){
        if(n%i==0)return false;
    }
    return true;
}
int solve(int x){
    memset(nums,0,sizeof nums);
    int idx = 0;
    while(x){
        nums[idx++]=x%10;
        x/=10;
    }
    for(int i = 0;i<idx;i++){
        for(int j = 0;j<idx;j++){
            if(nums[i]==0||i==j)continue;
            if(isPrime((10*nums[i]+nums[j])))return 1;
        }
    }
    return 0;
}
int main(){
    int a,b;
    cin>>a>>b;
    int ret = 0;
    for(int i = max(a,10);i<=b;i++){
        ret += solve(i);
    }
    cout<<ret<<endl;
    return 0;
}
```

## [DNA序列_牛客题霸_牛客网](https://www.nowcoder.com/practice/e8480ed7501640709354db1cc4ffd42a?tpId=37&tqId=21286&ru=/exam/oj)

```c++
#include <iostream>
#include <string>


using namespace std;


int main(){
    string s;
    int k;
    cin>>s>>k;
    int n = s.size(),start = 0,temp = 0,sum = 0;
    for(int left = 0,right = 0;right<n;right++){
        temp += (s[right]=='C')||s[right]=='G';
        while (right-left+1>k) {
            temp -= (s[left]=='C')||s[left]=='G';
            left++;
        }
        if(right-left+1==k&&temp>sum){
            sum = temp;
            start=left;
        }
    }
    cout<<s.substr(start,k)<<endl;
    return 0;
}
```

