| question                                                     | tag      |
| ------------------------------------------------------------ | -------- |
| [游游的you__牛客网](https://www.nowcoder.com/questionTerminal/cd117803b3364b218a8b3dcc498dee25) | 贪心     |
| [腐烂的苹果_牛客题霸_牛客网](https://www.nowcoder.com/practice/54ab9865ce7a45968b126d6968a77f34?tpId=196&tqId=40529&ru=/exam/oj) | BFS      |
| [大数加法_牛客题霸_牛客网](https://www.nowcoder.com/practice/11ae12e8c6fe48f883cad618c2e81475?tpId=196&tqId=37176&ru=/exam/oj) | 模拟     |
| [链表相加(二)_牛客题霸_牛客网](https://www.nowcoder.com/practice/c56f6c70fb3f4849bc56e33ff2a50b6b?tpId=196&tqId=37147&ru=/exam/oj) | 模拟     |
| [孩子们的游戏(圆圈中最后剩下的数)_牛客题霸_牛客网](https://www.nowcoder.com/practice/f78a359491e64a50bce2d89cff857eb6?tpId=13&tqId=11199&ru=/exam/oj) | 动态规划 |
| [大数乘法_牛客题霸_牛客网](https://www.nowcoder.com/practice/c4c488d4d40d4c4e9824c3650f7d5571?tpId=196&tqId=37177&ru=/exam/oj) | 模拟     |



## [游游的you__牛客网](https://www.nowcoder.com/questionTerminal/cd117803b3364b218a8b3dcc498dee25)

- 优先配对`you`，使结果最大

```c++
#include <iostream>

using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int a,b,c;
        cin>>a>>b>>c;
        int minVal = min(a,min(b,c));
        b-=minVal;
        if(b==0)b=1;
                   cout<<minVal*2+b-1<<endl;
    }
}
// 64 位输出请用 printf("%lld")
```



## [腐烂的苹果_牛客题霸_牛客网](https://www.nowcoder.com/practice/54ab9865ce7a45968b126d6968a77f34?tpId=196&tqId=40529&ru=/exam/oj)

- 统计完好的苹果的数量，同时吧所有腐烂的苹果添加到队列中
- 使用BFS搜索

```c++
#include <utility>
#include <vector>
class Solution {
    int n, m, num=0, ans=0;
    queue<pair<int, int>>q;
    int dx[4] {1, -1, 0, 0}, dy[4] {0, 0, 1, -1};
    void bfs(vector<vector<int> >& grid) {
        while (num&&!q.empty()) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                auto t = q.front();
                q.pop();
                for (int k = 0; k < 4; k++) {
                    int x = t.first + dx[k], y = t.second + dy[k];
                    if (x >= 0 && x < n && y >= 0 && y < m && grid[x][y] == 1) {
                        grid[x][y] = 2;
                        q.emplace(x, y);
                        --num;
                    }
                }
            }
            ++ans;
        }
    }
  public:
    int rotApple(vector<vector<int> >& grid) {
        // write code here
        n = grid.size(), m = grid[0].size();
        // 统计一共有多少个完好的苹果
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1)num++;
                else if (grid[i][j] == 2)q.emplace(i, j);
            }
        }
        bfs(grid);
        if (num)return -1;
        return ans;
    }
};
```

## [大数加法_牛客题霸_牛客网](https://www.nowcoder.com/practice/11ae12e8c6fe48f883cad618c2e81475?tpId=196&tqId=37176&ru=/exam/oj)

```c++
#include <algorithm>
#include <string>
class Solution {
public:
    string solve(string s, string t) {
        // write code here
        reverse(s.begin(), s.end());
        reverse(t.begin(),t.end());
        int n = s.size(),m = t.size(),carry=0;
        string result;
        for(int i = 0;i<n||i<m||carry;i++){
            int a =0,b=0;
            if(i<n)a = s[i]-'0';
            if(i<m)b=t[i]-'0';
            int t = a+b+carry;
            result.push_back('0'+t%10);
            carry=t/10;
        }
        reverse(result.begin(),result.end());
        return result;
    }
};
```

## [链表相加(二)_牛客题霸_牛客网](https://www.nowcoder.com/practice/c56f6c70fb3f4849bc56e33ff2a50b6b?tpId=196&tqId=37147&ru=/exam/oj)

- 和大数加法基本一致，只不过是使用链表来实现罢了

```c++
class Solution {
    // 反转链表
    ListNode* reverseList(ListNode* head){
        ListNode* cur = head,*prev = nullptr;
        while(cur){
            ListNode* next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }
  public:
    ListNode* addInList(ListNode* head1, ListNode* head2) {
        // write code here
        head1 = reverseList(head1);
        head2 = reverseList(head2);
        // 虚拟头结点
        ListNode dummy(-1);
        ListNode* cur = nullptr,*prev = &dummy;
        int carry = 0;
        while (head1||head2||carry) {
            int a = 0,b=0;
            if(head1){
                a = head1->val;
                head1 = head1->next;
            }
            if(head2){
                b = head2->val;
                head2 = head2->next;
            }
            int t = a+b+carry;
            cur = new ListNode(t%10);
            carry = t/10;
            prev->next = cur;
            prev = cur;
        }
        prev->next = nullptr;
        return reverseList(dummy.next);
    }
};
```



## [孩子们的游戏(圆圈中最后剩下的数)_牛客题霸_牛客网](https://www.nowcoder.com/practice/f78a359491e64a50bce2d89cff857eb6?tpId=13&tqId=11199&ru=/exam/oj)

![img](https://i-blog.csdnimg.cn/direct/b4d925333ce94f58b11104bf53b62431.png)

```c++
class Solution {
public:
    int LastRemaining_Solution(int n, int m) {
        // write code here
        int x = 0;
        for(int i = 2;i<=n;i++){
            x = (x+m)%i;
        }
        return x;
    }
};
```

## [大数乘法_牛客题霸_牛客网](https://www.nowcoder.com/practice/c4c488d4d40d4c4e9824c3650f7d5571?tpId=196&tqId=37177&ru=/exam/oj)

```c++
class Solution {
public:
    string solve(string s, string t) {
        // write code here
        reverse(s.begin(),s.end());
        reverse(t.begin(),t.end());
        int n = s.size(),m = t.size();
        vector<int>temp(n+m);
        for(int i = 0;i<n;i++){
            for(int j = 0;j<m;j++){
                temp[i+j] += (s[i]-'0')*(t[j]-'0');
            }
        }
        int c=0;
        string ret;
        for(auto&x:temp){
            c+=x;
            ret.push_back(c%10+'0');
            c/=10;
        }
        while(c){
            ret.push_back(c%10+'0');
            c/=10;
        }
        while(ret.size()>1&&ret.back()=='0')ret.pop_back();
        reverse(ret.begin(),ret.end());
        return ret;
    }
};
```

