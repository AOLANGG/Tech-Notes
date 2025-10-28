| question                                                     | tag      |
| ------------------------------------------------------------ | -------- |
| [小易的升级之路](https://www.nowcoder.com/share/jump/8978549211761610246104) | 模拟     |
| [礼物的最大价值](https://www.nowcoder.com/practice/2237b401eb9347d282310fc1c3adb134?tpId=265&tqId=39288&ru=/exam/oj) | 动态规划 |
| [对称之美](https://ac.nowcoder.com/acm/problem/214850)       | 双指针   |
| [连续子数组最大和](https://www.nowcoder.com/practice/1718131e719746e9a56fb29c40cc8f95?tpId=230&tqId=39753&ru=/exam/oj) | 贪心     |
| [非对称之美](https://ac.nowcoder.com/acm/problem/214851)     | 找规律   |
| [经此一役小红所向披靡](https://ac.nowcoder.com/acm/problem/223985) | 数学     |





## 小易的升级之路

```c++
#include <iostream>

using namespace std;
const int N = 1e5 + 10;
int n, c;
int gcd(int a, int b) {
    if (b == 0)return a;
    else return gcd(b, a % b);
}
int main() {
    while (cin >> n >> c) {
        while (n--) {
            int b;
            cin >> b;
            if (b <= c)c += b;
            else c += gcd(b, c);
        }
        cout << c << endl;
    }

    return 0;
}
```

## 礼物的最大价值

```c++
class Solution {
public:
    int maxValue(vector<vector<int> >& grid) {
        // write code here
        int n = grid.size(),m = grid[0].size();
        vector<vector<int> >f(n+1,vector<int>(m+1));
        // f[i][j] = max(f[i-1][j],f[i][j-1])
        for(int i = 1;i<=n;i++){
            for(int j = 1;j<=m;j++){
                f[i][j] = max(f[i-1][j],f[i][j-1])+grid[i-1][j-1];
            }
        }
        return f[n][m];
    }
};
```

## 对称之美

```c++
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

bool vis[110][26];
bool check(int i, int j) {
    for (int k = 0; k < 26; k++) {
        if (vis[i][k] && vis[j][k])return true;
    }
    return false;
}
int main() {
    int t;
    cin >> t;
    while (t--) {
        memset(vis, 0, sizeof vis);
        int n;
        cin >> n;
        for (int i = 0; i < n; i++) {
            string s;
            cin >> s;
            for (char& c : s) {
                vis[i][c - 'a'] = true;
            }
        }
        int left = 0, right = n - 1;
        while (left < right) {
            if (!check(left, right))break;
            left++, right--;
        }
        if (left < right)cout << "No" << endl;
        else cout << "Yes" << endl;
    }
    return 0;
}
```

## 连续子数组最大和

```c++
#include <climits>
#include <iostream>
using namespace std;
int n;

int main() {
    cin>>n;
    long long sum = 0;
    long long ret = INT_MIN;
    for(int i = 0;i<n;i++){
        int a;
        cin>>a;
        sum+=a;
        ret = max(ret,sum);
        if(sum<0)sum = 0;
    }    
    cout<<ret<<endl;
    return 0;
}
// 64 位输出请用 printf("%lld")
```



## 非对称之美

```c++
#include <iostream>
#include <string>

using namespace std;
bool isSymmetry(const string& s){
    int l = 0,r = s.size()-1;
    while(l<r){
        if(s[l++]!=s[r--])return false;
    }
    return true;
}
int main(){
    string s;
    cin>>s;
    if(!isSymmetry(s))cout<<s.size()<<endl;
    else{
        if(s==string(s.size(),s[0]))cout<<0<<endl;
        else cout<<s.size()-1<<endl;
    }
    return 0;
}
```



## 经此一役小红所向披靡

```c++
#include <iostream>
using namespace std;
typedef long long LL;
LL a, h, b, k;
int main()
{
	cin >> a >> h >> b >> k;

	LL ret = 0;
	// 1. 计算互砍多少回合
	LL n = min(h / b, k / a);
	ret += n * (a + b);

	// 2. 计算剩余⾎量
	h -= n * b;
	k -= n * a;

	// 3. 判断是否都还活着
	if (h > 0 && k > 0)
	{
		h -= b;
		k -= a;
		ret += a + b;
	}

	// 4. 判断是否会放⼤
	if (h > 0 || k > 0)
	{
		ret += 10 * (h > 0 ? a : b);
	}

	cout << ret << endl;

	return 0;
}
```

