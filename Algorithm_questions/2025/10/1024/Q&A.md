| question                                                     | tag    |
| ------------------------------------------------------------ | ------ |
| [游游的水果大礼包](https://ac.nowcoder.com/acm/problem/255193) | 枚举   |
| [买卖股票的最好时机(二)_牛客题霸_牛客网](https://www.nowcoder.com/practice/fbc5dad3e215457fb82a3ae688eb7281?tpId=230&tqId=39768&ru=/exam/oj) | 贪心   |
| [倒置字符串_牛客题霸_牛客网](https://www.nowcoder.com/practice/ee5de2e7c45a46a090c1ced2fdc62355?tpId=182&tqId=34788&ru=/exam/oj) | 双指针 |
| [删除公共字符_牛客题霸_牛客网](https://www.nowcoder.com/practice/f0db4c36573d459cae44ac90b90c6212?tpId=182&tqId=34789&ru=/exam/oj) | 模拟   |
| [两个链表的第一个公共结点_牛客题霸_牛客网](https://www.nowcoder.com/practice/6ab1d9a29e88450685099d45c9e31e46?tpId=13&tqId=11189&ru=/exam/oj) | 链表   |
| [mari和shiny](https://ac.nowcoder.com/acm/problem/26226)     | 前缀和 |



## [游游的水果大礼包](https://ac.nowcoder.com/acm/problem/255193)

```c++
#include <iostream>

int main()
{
    int n,m,a,b;
    std::cin>>n>>m>>a>>b;
    long long maxVal = 0;
    for(long long x = 0;x<=std::min(n/2,m);x++){
        long long y = std::min(n-2*x,(m-x)/2);
        if(y>=0){
            maxVal = std::max(maxVal,a*x+b*y);
        }
        if(2*x>n||x>m)break;;
    }
    std::cout<<maxVal<<std::endl;
    return 0;
}
```

## [买卖股票的最好时机(二)_牛客题霸_牛客网](https://www.nowcoder.com/practice/fbc5dad3e215457fb82a3ae688eb7281?tpId=230&tqId=39768&ru=/exam/oj)

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin>>n;
    vector<int>a(n);
    for(int i = 0;i<n;i++)cin>>a[i];
    int ret = 0;
    for(int i = 1;i<n;i++)
        if(a[i]-a[i-1]>0)
            ret += a[i]-a[i-1];
    cout<<ret<<endl;
    return 0;
}
// 64 位输出请用 printf("%lld")
```

## [倒置字符串_牛客题霸_牛客网](https://www.nowcoder.com/practice/ee5de2e7c45a46a090c1ced2fdc62355?tpId=182&tqId=34788&ru=/exam/oj)

```c++
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    getline(cin, s);
    reverse(s.begin(), s.end());
    int n = s.size();
    int right = 0;
    while(right<n){
        int left = right;
        while (right<n&&s[right]!=' ') {
            right++;
        }
        reverse(s.begin()+left,s.begin()+right);
        while (right<n&&s[right]==' ') {
            right++;
        }
    }
    cout<<s<<endl;
    return 0;
}
// 64 位输出请用 printf("%lld")
```

## [删除公共字符_牛客题霸_牛客网](https://www.nowcoder.com/practice/f0db4c36573d459cae44ac90b90c6212?tpId=182&tqId=34789&ru=/exam/oj)

```c++
#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

int main() {
    string s,t;
    getline(cin,s);
    getline(cin,t);
    unordered_set<char>st(t.begin(),t.end());
    for(char&c:s)
        if(!st.count(c))
            cout<<c;
    return 0;    
}
// 64 位输出请用 printf("%lld")
```

## [两个链表的第一个公共结点_牛客题霸_牛客网](https://www.nowcoder.com/practice/6ab1d9a29e88450685099d45c9e31e46?tpId=13&tqId=11189&ru=/exam/oj)

```c++
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* FindFirstCommonNode( ListNode* h1, ListNode* h2) {
        bool flag1 = false,flag2 = false;
		ListNode* head1 = h1,*head2 = h2;
		while(h1&&h2)
		{
			if(h1==h2)return h1;
			h1=h1->next;
			h2=h2->next;
			if(h1==nullptr&&!flag1){
				h1 = head2;
				flag1 = true;
			}
			if(h2==nullptr&&!flag2){
				h2 = head1;
				flag2 = true;
			}
		}
		return nullptr;
    }
};
```



## [mari和shiny](https://ac.nowcoder.com/acm/problem/26226)

```c++
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    string str;
    cin>>n>>str;
    vector<long long>s(n);
    s[0] = (str[0]=='s');
    auto y = s;
    y[n-1] = (str[n-1]=='y');
    for(int i = 1;i<n;i++)s[i] = s[i-1]+(str[i]=='s');
    for(int i=n-2;i>=0;i--)y[i] = y[i+1]+(str[i]=='y');
    long long ret = 0;
    for(int i=1;i<n-1;i++)
        if(str[i]=='h')
            ret+=s[i]*y[i];
    cout<<ret<<endl;
    return 0;
}
```

