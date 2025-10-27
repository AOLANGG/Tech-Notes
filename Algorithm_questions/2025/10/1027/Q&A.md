| question                                                     | tag       |
| ------------------------------------------------------------ | --------- |
| [小乐乐改数字_牛客题霸_牛客网](https://www.nowcoder.com/practice/fcd30aac9c4f4028b23919a0c649824d?tpId=290&tqId=39833&ru=/exam/oj) | 模拟      |
| [十字爆破](https://ac.nowcoder.com/acm/problem/205836)       | 前缀和    |
| [压缩字符串(一)_牛客题霸_牛客网](https://www.nowcoder.com/practice/c43a0d72d29941c1b65c857d8ac9047e?tpId=196&tqId=39317&ru=/exam/oj) | 双指针    |
| [比那名居的桃子](https://ac.nowcoder.com/acm/problem/224679) | 滑动窗口  |
| [01背包_牛客题霸_牛客网](https://www.nowcoder.com/practice/2820ea076d144b30806e72de5e5d4bbf?tpId=196&tqId=37561&ru=/exam/oj) | 01背包    |
| [chika和蜜柑](https://ac.nowcoder.com/acm/problem/26221)     | 排序/TOPK |





## [小乐乐改数字_牛客题霸_牛客网](https://www.nowcoder.com/practice/fcd30aac9c4f4028b23919a0c649824d?tpId=290&tqId=39833&ru=/exam/oj)

```c++
#include <iostream>
#include <cstring>

using namespace std;

int main(){
    char arr[10]{};
    scanf("%s",arr);
    int n = strlen(arr),ret = 0;
    for(int i = 0;i<n;i++){
        int x = arr[i]-'0';
        if(x&1)ret=ret*10+1;
        else ret=ret*10+0;
    }
    cout<<ret<<endl;
    return 0;
}
```

## [十字爆破](https://ac.nowcoder.com/acm/problem/205836)

```c++
#include <iostream>
#include <vector>

using namespace std;
int n,m;

int main(){
    scanf("%d%d",&n,&m);
    vector<vector<int> >grid(n+1,vector<int>(m+1));
    vector<long long>row(n+1);
    vector<long long>col(m+1);
    // 预处理每一行和每一列的前缀和
    for(int i = 1;i<=n;i++){
        long long sum = 0;
        for(int j = 1;j<=m;j++){
            scanf("%d",&grid[i][j]);
            sum+=grid[i][j];
        }
        row[i] = sum;
    }
    for(int j = 1;j<=m;j++){
        long long sum = 0;
        for(int i = 1;i<=n;i++){
            sum+=grid[i][j];
        }
        col[j] = sum;
    }
    for(int i=1;i<=n;i++){
        for(int j = 1;j<=m;j++){
            cout<<0ll+row[i]-grid[i][j]+col[j]<<' ';
        }
        cout<<'\n';
    }
    return 0;
}
```

## [压缩字符串(一)_牛客题霸_牛客网](https://www.nowcoder.com/practice/c43a0d72d29941c1b65c857d8ac9047e?tpId=196&tqId=39317&ru=/exam/oj)

```c++
#include <string>
class Solution {
public:
    string compressString(string param) {
        // write code here
        int n = param.size();
        string ret;
        for(int left = 0;left<n;){
            int right=left+1;
            while (right<n&&param[right]==param[right-1]) {
                right++;
            }
            int cnt = right-left;
            ret+=param[left];
            if(cnt==1){
                left = right;
                continue;
            }
            // cnt 不一定就是个个位数
            ret += to_string(cnt);
            left = right;

        }
        return ret;
    }
};
```

## [比那名居的桃子](https://ac.nowcoder.com/acm/problem/224679)

```c++
#include <iostream>
using namespace std;

int n, k;
const int N = 1e5 + 10;
long long a[N], b[N];  // 用long long避免溢出

int main() {
    cin >> n >> k;
    for (int i = 1; i <= n; i++) cin >> a[i];
    for (int i = 1; i <= n; i++) cin >> b[i];
    
    long long max_happy = -1;  // 初始化为最小值，确保第一个窗口被选中
    long long min_humiliation = 0;
    int best_day = 1;
    
    long long current_happy = 0;
    long long current_humiliation = 0;
    int left = 1;  // 定义left
    
    for (int right = 1; right <= n; right++) {
        current_happy += a[right];
        current_humiliation += b[right];
        
        // 窗口长度超过k时，移动左边界
        while (right - left + 1 > k) {
            current_happy -= a[left];
            current_humiliation -= b[left];
            left++;
        }
        
        // 窗口长度为k时判断
        if (right - left + 1 == k) {
            if (current_happy > max_happy) {
                max_happy = current_happy;
                min_humiliation = current_humiliation;
                best_day = left;
            } else if (current_happy == max_happy && current_humiliation < min_humiliation) {
                min_humiliation = current_humiliation;
                best_day = left;
            }
            // 快乐值和羞耻度都相等时，不更新（保留更早的best_day）
        }
    }
    
    cout << best_day << endl;
    return 0;
}
```

## [01背包_牛客题霸_牛客网](https://www.nowcoder.com/practice/2820ea076d144b30806e72de5e5d4bbf?tpId=196&tqId=37561&ru=/exam/oj)

```c++
#include <vector>
class Solution {
  public:
    int knapsack(int V, int n, vector<vector<int> >& vw) {
        // write code here
        vector<int>dp(V+1);
        for (int i = 1; i <= n; ++i) {
            for (int j = V; j >= vw[i - 1][0]; --j) {
                dp[j] = max(dp[j], dp[j - vw[i - 1][0]] + vw[i - 1][1]);
            }
        }
        return dp[V];
    }
};
```



## [chika和蜜柑](https://ac.nowcoder.com/acm/problem/26221)

```c++
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int n, k;
const int N = 2e5 + 10;
int a[N], b[N];

struct com {
    bool operator()(const pair<int, int>& x, const pair<int, int>& y) {
        if (x.first != y.first) {
            return x.first > y.first;
        } else {
            return x.second < y.second;
        }
    }
};

int main() {
    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
    }
    priority_queue<pair<int, int>, vector<pair<int, int>>, com> q;

    for (int i = 0; i < n; ++i) {
        q.emplace(b[i], a[i]);
        if (q.size() > k) {
            q.pop();
        }
    }
    long long total_acidity = 0, total_sweetness = 0;
    while (!q.empty()) {
        auto curr = q.top();
        q.pop();
        total_sweetness += curr.first;
        total_acidity += curr.second;
    }

    cout << total_acidity << " " << total_sweetness << endl;

    return 0;
}
```

