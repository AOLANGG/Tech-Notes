| question                                                     | tag         |
| ------------------------------------------------------------ | ----------- |
| [爱丽丝的人偶](https://ac.nowcoder.com/acm/problem/213471)   | 模拟        |
| [集合](https://www.nowcoder.com/practice/635ff765d4af45b5bf8e3756ed415792?tpId=134&tqId=33860&ru=/exam/oj) | 排序+双指针 |
| [最长回文子序列](https://www.nowcoder.com/practice/82297b13eebe4a0981dbfa53dfb181fa?tpId=230&tqId=39762&ru=/exam/oj) | 区间DP      |
| [数组变换](https://www.nowcoder.com/questionTerminal/c55f4f15cc3f4ff0adede7f9c69fa0c1) | 找规律      |
| [装箱问题](https://ac.nowcoder.com/acm/problem/16693)        | 01背包      |
| [添加字符](https://www.nowcoder.com/questionTerminal/b2b816e20e8343b49abbaf493886ce26) | 模拟        |



## 爱丽丝的人偶

```c++
#include <iostream>

using namespace std;
const int N = 1e5+10;
int n,a[N];

int main(){
    cin>>n;
    int num = 1;
    for(int i = 0;num<=n;i+=2){
        if(i>=n)i = 1;
        a[i] = num++;
    }
    for(int i = 0;i<n;i++)cout<<a[i]<<' ';
    cout<<'\n';
    return 0;
}
```

## 集合

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n,m;
    cin>>n>>m;
    vector<int>a(n),b(m),merge;
    for(int i = 0;i<n;i++)cin>>a[i];
    for(int i = 0;i<m;i++)cin>>b[i];
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int i=0,j=0;
    for(;i<n&&j<m;){
        if(a[i]<b[j])merge.emplace_back(a[i++]);
        else if(a[i]==b[j]){
            merge.emplace_back(a[i++]);
            j++;
        }
        else merge.emplace_back(b[j++]);
    }
    while(i<n)merge.emplace_back(a[i++]);
    while(j<m)merge.emplace_back(b[j++]);
    for(int&x:merge)cout<<x<<' ';
    cout<<'\n';
    return 0;    
}
// 64 位输出请用 printf("%lld")
```

## 最长回文子序列

![img](https://i-blog.csdnimg.cn/direct/6edc1ae9fd2347de910eba167285d7cf.png)

```c++
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    string s;
    cin>>s;
    int n = s.size();
    //f[i][j]表示[i,j]区间中的最长回文子序列的长度是多少
    // s[i]==s[j] f[i][j] = f[i+1][j-1]+2;
    vector<vector<int> >f(n,vector<int>(n));
    for(int i = n-1;i>=0;i--){
        for(int j = i;j<n;j++){
            if(i==j)f[i][j] = 1;
            else{
                if(s[i]==s[j])f[i][j] = f[i+1][j-1]+2;
                else f[i][j] = max(f[i+1][j],f[i][j-1]);
            }
        }
    }
    cout<<f[0][n-1]<<endl;
    return 0;
}
```

## 数组变换

```c++
#include <iostream>
#include <vector>

using namespace std;
int slove(int x){
    while(x%2==0)x/=2;
    return x;
}
int main() {
    int n;
    cin>>n;
    vector<int>a(n);
    for(int i = 0;i<n;i++)cin>>a[i];
    int num = -1;
    for(int&x:a){
        int t = slove(x);
        if(num==-1)num = t;
        else if(num!=t){
            cout<<"NO"<<endl;
            return 0;
        }
    }
    cout<<"YES"<<endl;
    return 0;    
}
```

## 装箱问题

```c++
#include <iostream>
#include <vector>

using namespace std;

int main(){
    int V,n;
    cin>>V>>n;
    vector<int>a(n);
    for(int&x:a)cin>>x;
    // f[i][j]表示从前i个物品中挑选，体积不超过j的最大容量是多少
    vector<vector<int> >f(n+1,vector<int>(V+1));
    for(int i = 1;i<=n;i++){
        for(int j = 0;j<=V;j++){
            f[i][j] = f[i-1][j];
            if(j>=a[i-1])f[i][j] = max(f[i][j],f[i-1][j-a[i-1]]+a[i-1]);
        }
    }
    cout<<V-f[n][V]<<endl;
    return 0;
}
```

## 添加字符

```c++
#include <iostream>
#include <climits>
#include <string>

using namespace std;

int main(){
    int ret = INT_MAX;
    string a,b;
    cin>>a>>b;
    int m = a.size(),n = b.size();
    for(int i = 0;i<=n-m;i++){
        // 枚举b的起始位置
        int temp = 0;
        for(int j = 0;j<m;j++){
            if(a[j]!=b[i+j])temp++;
        }
        ret = min(ret,temp);
    }
    cout<<ret<<endl;
    return 0;
}
```

