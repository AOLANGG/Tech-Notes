| question                                                     | tag              |
| ------------------------------------------------------------ | ---------------- |
| [打怪](https://ac.nowcoder.com/acm/problem/202487)           | 数学             |
| [字符串分类](https://www.nowcoder.com/questionTerminal/9fbb4d95e6164cd9ab52e859fbe8f4ec) | 哈希表           |
| [城市群数量](https://www.nowcoder.com/practice/71cde4dee669475f94d8d38832374ada?tpId=196&tqId=40411&ru=/exam/oj) | 并查集           |
| [判断是不是平衡二叉树](https://www.nowcoder.com/practice/8b3b95850edb4115918ecebdf1b4d222?tpId=13&tqId=11192&ru=/exam/oj) | 平衡二叉树的判断 |
| [最大子矩阵](https://www.nowcoder.com/practice/a5a0b05f0505406ca837a3a76a5419b3?tpId=230&tqId=40416&ru=/exam/oj) | 二维前缀和       |
| [小葱的01串](https://ac.nowcoder.com/acm/problem/230830)     | 滑动窗口         |


## 打怪

```c++
#include <iostream>

using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int h,a,H,A;
        cin>>h>>a>>H>>A;
        if(a>=H){
            cout<<-1<<endl;
            continue;
        }
        // 杀死一个怪兽，需要攻击多少次
        int cnt = (H+a-1)/a;
//         cout<<"cnt: "<<cnt<<endl;
        // 掉血为
        int x = (cnt-1)*A;
//         cout<<"x: "<<x<<endl;
        // 最后一定要留一滴血，保证自己是活的
        cout<<(h-1)/x<<endl;
    }
    return 0;
}
```

## 字符串分类

```c++
#include <iostream>
#include <string>
#include <unordered_set>
#include <algorithm>

using namespace std;

int main() {
    unordered_set<string>st;
    int n;
    cin>>n;
    while(n--){
        string s;
        cin>>s;
        sort(s.begin(),s.end());
        st.insert(s);
    }
    cout<<st.size()<<endl;
    return 0;
}
// 64 位输出请用 printf("%lld")
```

## 城市群数量

```c++
class UnionSet
{
public:
    UnionSet(int n)
    {
        _ufs.resize(n,-1);
    }
    int findRoot(int x){
        if(_ufs[x]<0)return x;
        else return _ufs[x]=findRoot(_ufs[x]);
    }
    bool isSet(int x,int y){
        return findRoot(x)==findRoot(y);
    }
    void Union(int x,int y){
        int fx = findRoot(x),fy = findRoot(y);
        if(fx==fy)return;
        _ufs[fx]+=_ufs[fy];
        _ufs[fy] = fx;
    }
    int Count(){
        int cnt = 0;
        for(int&x:_ufs)
            if(x<0)
                cnt++;
        return cnt;
    }
private:
    vector<int>_ufs;
};
class Solution {
public:
    int citys(vector<vector<int> >& m) {
        int n = m.size();
        UnionSet ufs(n);
        for(int i = 0;i<n;i++){
            for(int j = 0;j<n;j++){
                if(m[i][j])
                    ufs.Union(i,j);
            }
        }
        return ufs.Count();
    }
};
```

## 判断是不是平衡二叉树

```c++
class Solution {
    int getHeight(TreeNode* node){
        if(node==nullptr)return 0;
        int Lh = getHeight(node->left);
        int rh = getHeight(node->right);
        if(Lh==-1||rh==-1||abs(Lh-rh)>1)return -1;
        else return max(Lh,rh)+1;
    }
public:
    bool IsBalanced_Solution(TreeNode* pRoot) {
        return getHeight(pRoot)!=-1;
    }
};
```

## 最大子矩阵

```c++
#include <iostream>
#include <climits>

using namespace std;
const int N = 105;
int g[N][N],n;

int main(){
    cin>>n;
    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=n;j++){
            cin>>g[i][j];
            g[i][j]+=g[i-1][j]+g[i][j-1]-g[i-1][j-1];
        }
    }
    int ret = INT_MIN;
    for(int x1 = 1;x1<=n;x1++){
        for(int y1 = 1;y1<=n;y1++){
            for(int x2 = x1;x2<=n;x2++){
                for(int y2 = y1;y2<=n;y2++){
                    ret = max(ret,g[x2][y2]-g[x1-1][y2]-g[x2][y1-1]+g[x1-1][y1-1]);
                }
            }
        }
    }
    cout<<ret<<endl;
    return 0;
}
```

## 小葱的01串

```c++
#include <iostream>
#include <string>

using namespace std;

int main(){
	int n;
	cin>>n;
	string s;
	cin>>s;
	int sum = 0,ret = 0,temp = 0;
	for(const char& ch:s)
		sum += ch-'0';
	for(int left = 0,right = 0;right<n-1;right++){
		temp += s[right]-'0';
		while(right-left+1>n/2)temp-=s[left++]-'0';
		if(right-left+1==n/2&&temp*2==sum){
			ret++;
		}
	}
	cout<<ret*2<<endl;
	return 0;
}
```

