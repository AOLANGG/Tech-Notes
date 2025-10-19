| question                                                     | tag            |
| ------------------------------------------------------------ | -------------- |
| [数字统计](https://www.nowcoder.com/share/jump/8978549211760841579812) | 简单数学       |
| [两个数组的交集](https://www.nowcoder.com/share/jump/8978549211760842152303) | 哈希表         |
| [点击消除](https://www.nowcoder.com/share/jump/8978549211760842368277) | 栈             |
| [牛牛的快递](https://www.nowcoder.com/share/jump/8978549211760843908944) | 模拟           |
| [数组中两个字符串的最小距离]()                               | 字符串，双指针 |



## 数字统计

- 统计`[l，r]`中每一个数的所有2的个数

```c++
#include <iostream>
using namespace std;
int count(int x)
{
    int cnt = 0;
    while(x)
    {
        if(x%10==2)cnt++;
        x/=10;
    }
    return cnt;
}
int main() {
    int l,r;
    cin>>l>>r;
    int ans = 0;
    for(int i = l;i<=r;i++)
        ans += count(i);
    cout<<ans<<endl;
    return 0;
}
// 64 位输出请用 printf("%lld")
```

## 两个数组的交集

- 用无序集合存`nums1`，遍历`nums2`中的元素，到`nums1`中查找，符合就添加到结果，为了防止重复添加，每次添加完成之后应当删除掉无序集合中的对应元素。

```c++
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int>ust(nums1.begin(),nums1.end());
        vector<int>result;
        for(int&x:nums2){
            if(ust.count(x)){
                result.emplace_back(x);
                ust.erase(x);
            }
        }
        return result;
    }
};
```

## 点击消除

- 直接用字符串模拟栈就行了

```c++
#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    cin>>s;
    string st;
    for(char&c:s){
        if(st.empty()||st.back()!=c){
            st.push_back(c);
        }else{
            st.pop_back();
        }
    }
    cout<<(st.empty()?"0":st)<<endl;
}
// 64 位输出请用 printf("%lld")
```

## 牛牛的快递



```c++
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    float a;
    char b;
    cin>>a>>b;
    if(a<=1)
    {
        cout<<20+(b=='y'?5:0);
    }
    else {
        cout<<20+ceil(a-1)+(b=='y'?5:0);
    }
    return 0;
}
// 64 位输出请用 printf("%lld")
```

## 数组中两个字符串的最小距离

```c++
#include <iostream>
#include <string>
#include <vector>
#include <climits>

using namespace std;

int main() {
    int n;
    cin>>n;
    string s,t;
    cin>>s>>t;
    string str;
    int i = -1,j = -1,ans = INT_MAX;
    for(int k = 0;k<n;k++)
    {
        cin>>str;
        if(str==s)i = k;
        else if(str==t)j = k;
        if(i!=-1&&j!=-1)ans = min(ans,abs(j-i));
    }
    cout<<(ans==INT_MAX?-1:ans)<<endl;
    return 0;
}
// 64 位输出请用 printf("%lld")
```

