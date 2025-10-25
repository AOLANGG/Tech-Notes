| question                                                     | tag      |
| ------------------------------------------------------------ | -------- |
| [牛牛冲钻五](https://ac.nowcoder.com/acm/problem/227309)     | 模拟     |
| [最长无重复子数组_牛客题霸_牛客网](https://www.nowcoder.com/practice/b56799ebfd684fb394bd315e89324fb4?tpId=196&tqId=37149&ru=/exam/oj) | 滑动窗口 |
| [重排字符串](https://ac.nowcoder.com/acm/problem/222104)     | 找规律   |
| [乒乓球筐__牛客网](https://www.nowcoder.com/questionTerminal/bb4f1a23dbb84fd7b77be1fbe9eaaf32) | 哈希表   |
| [组队竞赛_牛客笔试题_牛客网](https://www.nowcoder.com/questionTerminal/6736cc3ffd1444a4a0057dee89be789b) | 贪心     |
| [删除相邻数字的最大分数_牛客题霸_牛客网](https://www.nowcoder.com/practice/3bcf72c738b6494bbe1ebe0ffde56152?tpId=230&tqId=40419&ru=/exam/oj) | 动态规划 |



## [牛牛冲钻五](https://ac.nowcoder.com/acm/problem/227309)

```c++
#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--){
        int n,k;
        cin>>n>>k;
        int cnt = 0;
        string s;
        cin>>s;
        int ret = 0;
        for(char&c:s){
            if(c=='W'){
                cnt++;
                if(cnt>=3)ret+=k;
                else ret++;
            }
            else{
                cnt = 0;
                ret--;
            }
        }
        cout<<ret<<endl;
    }
    return 0;
}
```

## [最长无重复子数组_牛客题霸_牛客网](https://www.nowcoder.com/practice/b56799ebfd684fb394bd315e89324fb4?tpId=196&tqId=37149&ru=/exam/oj)

```c++
class Solution {
public:
    int maxLength(vector<int>& arr) {
        // write code here
        int n = arr.size();
        unordered_map<int,int>hashMap;
        int ret = 1;
        for(int left = 0,right = 0;right<n;right++){
            int in = arr[right];
            hashMap[in]++;
            while(left<right&&hashMap[in]>1)
            {
                int out = arr[left++];
                hashMap[out]--;
            }
            ret = max(ret,right-left+1);
        }
        return ret;
    }
};
```

## [重排字符串](https://ac.nowcoder.com/acm/problem/222104)

- 分奇偶位置填入

```c++
#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
    string s;
    cin>>n>>s;
    int hashMap[26]{};
    char maxChar;
    int maxCount = 0;
    for(char&c:s){
        if(maxCount<++hashMap[c-'a']){
            maxChar = c;
            maxCount = hashMap[c-'a'];
        }
    }
    if(2*maxCount-n>1)cout<<"no"<<endl;
    else{
        cout<<"yes"<<endl;
        string ret(n,' ');
        int index = 0;
        while(maxCount--){
            ret[index]=maxChar;
            index+=2;
        }
        for(int i = 0;i<26;i++){
            if(hashMap[i]&&i!=maxChar-'a'){
                while(hashMap[i]--){
                    if(index>=n)index = 1;
                    ret[index]=i+'a';
                    index+=2;
                }
            }
        }
        cout<<ret<<endl;
    }
    return 0;
}
```

## [乒乓球筐__牛客网](https://www.nowcoder.com/questionTerminal/bb4f1a23dbb84fd7b77be1fbe9eaaf32)

```c++
#include <iostream>
#include <string>
using namespace std;
int main() {
    string s1, s2;
    while (cin >> s1 >> s2) { // 未知组数的输⼊
        int hash[26] = { 0 };
        for (auto ch : s1) hash[ch - 'A']++;
        bool ret = true;
        for (auto ch : s2) {
            if (--hash[ch - 'A'] < 0) {
                ret = false;
                break;
            }
        }
        cout << (ret ? "Yes" : "No") << endl;
    }
    return 0;
}
```

## [组队竞赛_牛客笔试题_牛客网](https://www.nowcoder.com/questionTerminal/6736cc3ffd1444a4a0057dee89be789b)

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin>>n;
    vector<int>a(n*3);
    for(int&x:a)cin>>x;
    sort(a.begin(),a.end(),greater<int>());
    long long ret = 0;
    int index = 1,cnt = 0;
    while(cnt<n){
        ret += a[index];
        index+=2;
        cnt++;
    }
    cout<<ret<<endl;
    return 0;
}
// 64 位输出请用 printf("%lld")
```

## [删除相邻数字的最大分数_牛客题霸_牛客网](https://www.nowcoder.com/practice/3bcf72c738b6494bbe1ebe0ffde56152?tpId=230&tqId=40419&ru=/exam/oj)

```c++
#include <iostream>
using namespace std;
const int N = 1e4+10;
int f[N],g[N],hashMap[N];

int main() {
    int n;
    cin>>n;
    for(int i = 0;i<n;i++){
        int x;
        cin>>x;
        hashMap[x]+=x;
    }
    // f[i]=hashMap[i]+g[i-1]
    // g[i] = max(f[i-1],g[i-1])
    for(int i = 1;i<N;i++){
        f[i] = hashMap[i]+g[i-1];
        g[i] = max(f[i-1],g[i-1]);
    }
    cout<<max(f[N-1],g[N-1])<<endl;
    return 0;
}
// 64 位输出请用 printf("%lld")
```

