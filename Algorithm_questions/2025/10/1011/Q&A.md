| question                                                     | tag            |
| ------------------------------------------------------------ | -------------- |
| [组合总和](https://leetcode.cn/problems/combination-sum?envType=study-plan-v2&envId=top-100-liked) | 暴搜+剪枝      |
| [括号生成](https://leetcode.cn/problems/generate-parentheses?envType=study-plan-v2&envId=top-100-liked) | 回溯           |
| [单词搜索](https://leetcode.cn/problems/word-search?envType=study-plan-v2&envId=top-100-liked) | 深搜、回溯     |
| [分隔回文串](https://leetcode.cn/problems/palindrome-partitioning?envType=study-plan-v2&envId=top-100-liked) | 回溯           |
| [N皇后]()                                                    | 回溯           |
| [搜索插入位置](https://leetcode.cn/problems/search-insert-position?envType=study-plan-v2&envId=top-100-liked) | 二分查找       |
| [搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix?envType=study-plan-v2&envId=top-100-liked) | 二分查找，矩阵 |



## 组合总和

- 每个位置考虑选或者不选
- 遍历的过程中，还要进行检验当前的和
  - 如果当前的和已经等于`target`，把当前的路径存储到结果中
  - 如果当前的和已经大于`target`，直接`return`返回，因为`candidates`中所有的值都是大于`0`的，继续遍历不可能得到结果（及时止损）

```c++
class Solution {
    vector<vector<int> >result;
    int aim;
    vector<int>path;
    void dfs(const vector<int>&candidates,int u,int sum)
    {
        if(sum == aim){
            result.push_back(path);
            return;
        }
        if(sum>aim||u ==candidates.size())return;
        for(int i = u;i<candidates.size();i++)
        {
            path.push_back(candidates[i]);
            dfs(candidates,i,sum+candidates[i]);
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        aim = target;
        dfs(candidates,0,0);
        return result;
    }
};
```

## 括号生成

**暴力做法**（可以通过）

- 直接暴力搜索每个位置是`(`还是`)`，让这个字符串的大小为`2*n`
- 最后搜索出来，检验是否是有效的括号
  - 是的话，添加到结果中

```c++
class Solution {
    bool isValid(string s) {
        if (s.size() % 2)
            return false;
        stack<char> st;
        for (const char c : s) {
            if (c == '(')
                st.push(')');
            else if (c == '[')
                st.push(']');
            else if (c == '{')
                st.push('}');
            else if(st.empty()||st.top()!=c)
                return false;
            else
                st.pop();
        }
        return st.empty();
    }
    vector<string>result;
    string path;
    void dfs(int u,int n)
    {
        if(u==n*2)
        {
            if(isValid(path))
                result.push_back(path);
            return;
        }
        path.push_back('(');
        dfs(u+1,n);
        path.pop_back();
        path.push_back(')');
        dfs(u+1,n);
        path.pop_back();
    }
public:
    vector<string> generateParenthesis(int n) {
        dfs(0,n);
        return result;
    }
};
```

**更高效的做法**

- 因为只有`()`一种样式的括号，所以有一个性质——左括号的数量必须大于右括号的数量，利用这个性质解决本题可以更加的高效

```c++
class Solution {
public:
    vector<string>result;
    string path;
    int left = 0,right= 0;
    void dfs(int n,int pos)
    {
        if(left<right)return;
        if(pos == 2*n){
            if(left == right)result.push_back(path);
            return;
        }

        left++;
        path.push_back('(');
        dfs(n,pos+1);
        path.pop_back();
        left--;

        right++;
        path.push_back(')');
        dfs(n,pos+1);
        path.pop_back();
        right--;
    }
    vector<string> generateParenthesis(int n) {
        dfs(n,0);
        return result;
    }
};
```

## 单词搜索

```c++
class Solution {
    bool vis[10][10];
    int n,m;
    int dx[4] = {0,0,-1,1},dy[4] = {-1,1,0,0};
    bool dfs(const vector<vector<char> >&board,const string& word,int i,int j,int u)
    {
        if(u==word.size())return true;
        vis[i][j] = true;
        for(int k = 0;k<4;k++)
        {
            int x = i+dx[k],y=j+dy[k];
            if(x>=0&&x<n&&y>=0&&y<m&&!vis[x][y]&&board[x][y] == word[u])
            {
                if(dfs(board,word,x,y,u+1))return true;
            }
        }
        vis[i][j]=false;
        return false;
    }
public:
    bool exist(vector<vector<char>>& board, string word) {
        n = board.size(),m = board[0].size();
        for(int i = 0;i<n;i++)
        {
            for(int j = 0;j<m;j++)
            {
                if(board[i][j] == word[0])
                {
                    if(dfs(board,word,i,j,1))return true;
                }
            }
        }
        return false;
    }
};
```

## 分隔回文串



```c++
class Solution {
    bool is_palindrome(const string& s,int left,int right)
    {
        while(left<right)
        {
            if(s[left++]!=s[right--])
            {
                return false;
            }
        }
        return true;
    }
    vector<vector<string> >result;
    vector<string>path;
    int n;
    void dfs(int u,int start,const string& s)
    {
        if(u==n)
        {
            result.emplace_back(path);
            return;
        }
        // 不选择当前的这个逗号
        if(u!=n-1)
        {
            dfs(u+1,start,s);
        }
        // 选择当前的逗号，但是需要保证回文的条件
        if(is_palindrome(s,start,u))
        {
            path.emplace_back(s.substr(start,u-start+1));
            dfs(u+1,u+1,s);
            path.pop_back();
        }
    }
public:
    vector<vector<string>> partition(string s) {
        n = s.size();
        dfs(0,0,s);
        return result;
    }
};
```

## N皇后

- 枚举每一行
- 每次枚举的时候，需要检查列、主对角线和副对角线

```c++
class Solution {
    vector<vector<string> >ret;
    vector<string>path;
    bool checkCol[10],checkDig1[20],checkDig2[20];
    int n;
    void dfs(int row)
    {
        if(row==n)
        {
            ret.emplace_back(path);
            return;
        }
        for(int col = 0;col<n;col++)
        {
            if(checkCol[col]==false&&checkDig1[row-col+n]==false&&checkDig2[row+col]==false){
                path[row][col] = 'Q';
                checkCol[col]=true;
                checkDig1[row-col+n]=true;
                checkDig2[row+col]=true;
                dfs(row+1);
                path[row][col] = '.';
                checkCol[col]=false;
                checkDig1[row-col+n]=false;
                checkDig2[row+col]=false;
            }
        }
    }
public:
    vector<vector<string>> solveNQueens(int _n) {
        n = _n;
        path.resize(n,string(n,'.'));
        dfs(0);
        return ret;
    }
};
```

## 搜索插入位置

- 数组中不存在`target`的情况，需要进行特判

```c++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();
        int left = 0,right = n-1;
        while(left<right)
        {
            int mid = left+(right-left)/2;
            if(nums[mid]>=target)right = mid;
            else left = mid+1;
        }
        if(nums[left]<target)return left+1;
        return left;
    }
};
```

## 搜索二维矩阵

- 有右上角（或者左下角），按照二分的思想进行搜索即可

```c++
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // 从右上角开始搜索
        int n = matrix.size(),m = matrix[0].size();
        int row = 0,col = m-1;
        while(row<n&&col>=0)
        {
            if(matrix[row][col]>target)col--;
            else if(matrix[row][col]<target)row++;
            else return true;
        }
        return false;
    }
};
```

