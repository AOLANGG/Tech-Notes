| question                                                     | tag       |
| ------------------------------------------------------------ | --------- |
| [笨小猴](https://www.nowcoder.com/practice/17865bc2a75c4944a872ef709958c56e?tpId=290&tqId=39933&ru=/exam/oj) | 哈希表    |
| [**NC383** **主持人调度（一）**](https://www.nowcoder.com/practice/e160b104354649b69600803184094adb?tpId=196&tqId=40514&ru=/exam/oj) | 排序      |
| [**分割等和子集**](https://www.nowcoder.com/practice/65ade309fa4d4067a9add749721bfdc0?tpId=230&tqId=40433&ru=/exam/oj) | 01背包    |
| [小红的ABC](https://ac.nowcoder.com/acm/problem/230720)      | 模拟      |
| [**不相邻取数**](https://www.nowcoder.com/practice/a2be806a0e5747a088670f5dc62cfa1e?tpId=230&tqId=39763&ru=/exam/oj) | 动态规划  |
| [空调遥控](https://ac.nowcoder.com/acm/problem/229310)       | 排序+二分 |



## 笨小猴

```c++
#include <climits>
#include <iostream>
#include <string>
using namespace std;
int hashMap[26];

bool isPrime(int n){
    for(int i = 2;i<=n/i;i++){
        if(n%i==0)return false;
    }
    return n>=2;
}
int main() {
    string word;
    cin>>word;
    int maxn = INT_MIN,minn=INT_MAX;
    for(const char& ch:word){
        hashMap[ch-'a']++;
    }
    for(int i = 0;i<26;i++){
        if(hashMap[i]){
            maxn=max(maxn,hashMap[i]);
            minn=min(minn,hashMap[i]);
        }
    }
    if(isPrime(maxn-minn)){
        cout<<"Lucky Word\n"<<maxn-minn<<'\n';
    }
    else{
        cout<<"No Answer\n"<<0<<'\n';
    }
}
// 64 位输出请用 printf("%lld")
```

## **NC383** **主持人调度（一）**

```c++
class Solution {
  public:
    bool hostschedule(vector<vector<int> >& schedule) {
        // write code here
        int n = schedule.size();
        sort(schedule.begin(), schedule.end());
        int s = schedule[0][0], e = schedule[0][1];
        for (int i = 1; i < n; i++) {
            if (e > schedule[i][0]) {
                return false;
            }
            else{
                s = schedule[i][0], e = schedule[i][1];
            }
        }
        return true;
    }
};
```

## **分割等和子集**

```c++
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int>a(n);
    int sum = 0;
    for (int& x : a) {
        cin >> x;
        sum += x;
    }
    if (sum % 2) {
        cout << "false" << endl;
    }
    else {
        int target = sum / 2;
        vector<vector<bool> >f(n + 1, vector<bool>(target + 1));
        // f[i][j]表示从前i个元素中挑选，总和为j的情况是否存在
        // 初始化
        f[0][0] = true;
        // 填表
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= target; j++) {
                f[i][j] = f[i - 1][j];
                if (j >= a[i - 1])f[i][j] = f[i][j] || f[i - 1][j - a[i - 1]];
            }
        }
        if (f[n][target])cout << "true" << endl;
        else cout << "false" << endl;
    }

    return 0;
}
```

## 小红的ABC

```c++
#include <iostream>
#include <string>

using namespace std;

int main(){
    string s;
    cin>>s;
    int n = s.size();
    int ret = -1;
    for(int i = 0;i<n;i++){
        if(i+1<n&&s[i]==s[i+1]){
            ret = 2;
            break;
        }
        else if(i+2<n&&s[i]==s[i+2]){
            ret = 3;
        }
    }
    cout<<ret<<endl;
    return 0;
}
```

## **不相邻取数**

```c++
#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    cin>>n;
    vector<int>a(n+1);
    for(int i = 1;i<=n;i++)cin>>a[i];
    int ret = 0;
    vector<int>f(n+1);
    auto g = f;
    // f[i]表示前i个元素中挑选，第i个元素必选，这种情况下的数的最大和
    // g[i]表示前i个元素中挑选，第i个元素不选，这种情况下的数的最大和
    for(int i = 1;i<=n;i++){
        f[i] = g[i-1]+a[i];
        g[i] = max(f[i-1],g[i-1]);
        ret = max(ret,max(f[i],g[i]));
    }
    cout<<ret<<endl;
    return 0;
}
```

## 空调遥控

```c++
// CSDN：https://blog.csdn.net/2301_79420799?spm=1010.2135.3001.5343
#include <iostream>
#include <climits>
#include <algorithm>

using namespace std;
const int N = 1000000 + 10;
int n, p, a[N];
// 查找>=x的最小的下标
int Left(int x) {
	int l = 0, r = n - 1;
	while (l < r) {
		int mid = l + (r - l) / 2;
		if (a[mid] >= x)r = mid;
		else l = mid + 1;
	}
	return l;
}
// 查找<=x的最小的下标
int Right(int x) {
	int l = 0, r = n - 1;
	while (l < r) {
		int mid = l + (r - l + 1) / 2;
		if (a[mid] <= x)l = mid;
		else r = mid - 1;
	}
	return l;
}
int main() {
	cin >> n >> p;
	int mi = INT_MAX, ma = INT_MIN;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		ma = max(ma, a[i]);
		mi = min(mi, a[i]);
	}
	sort(a, a + n);
	int ret = 0;
	for (int i = mi; i <= ma; i++) {
		int l = Left(i - p), r = Right(i + p);
		ret = max(ret, r - l + 1);
	}
	cout << ret << endl;
	return 0;
}
```

