| question                                                     | tag               |
| ------------------------------------------------------------ | ----------------- |
| [二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree?envType=study-plan-v2&envId=top-100-liked) | 二叉树            |
| [二叉树的最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum?envType=study-plan-v2&envId=top-100-liked) | 二叉树            |
| [岛屿数量](https://leetcode.cn/problems/number-of-islands?envType=study-plan-v2&envId=top-100-liked) | 深度搜索/广度搜索 |
| [腐烂的橘子](https://leetcode.cn/problems/rotting-oranges?envType=study-plan-v2&envId=top-100-liked) | BFS               |
| [课程表](https://leetcode.cn/problems/course-schedule?envType=study-plan-v2&envId=top-100-liked) | 拓扑排序          |



## 二叉树的最近公共祖先

- 题目中给定`p`和`q`均存在于给定的二叉树中，是一定有结果的
- 按照后序遍历的方式进行遍历二叉树
- 每次找到`p`或者`q`的时候就返回该节点（指针）

```c++
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root==nullptr)return nullptr;
        if(root==p||root==q)return root;
        TreeNode* left = lowestCommonAncestor(root->left,p,q);
        TreeNode* right = lowestCommonAncestor(root->right,p,q);
        if(left&&right)return root;
        else if(left==nullptr&&right)return right;
        else if(left&&right==nullptr)return left;
        return nullptr;
    }
};
```

## 二叉树的最大路径和

- 遍历到每个节点的时候，递归左子树和右子树（它们返回的值可以是0）
- 加上节点对应的值，来更新结果

```c++
class Solution {
    int ans = INT_MIN;
    int dfs(TreeNode* node)
    {
        if(node==nullptr)return 0;
        int l_val = dfs(node->left);
        int r_val = dfs(node->right);
        ans = max(ans,l_val+r_val+node->val);
        return max(max(l_val,r_val)+node->val,0);
    }
public:
    int maxPathSum(TreeNode* root) {
        dfs(root);
        return ans;
    }
};
```

## 岛屿数量

- 使用搜索的遍历方法，找到一个符合添加的岛屿节点，搜索这个节点所在的岛屿的全部节点，标记这些节点
- 继续遍历整个二维网格，统计所有的岛屿数量

*这里使用`DFS`的做法*

```c++
class Solution {
    int n,m;
    vector<vector<bool> >vis; 
    int dx[4]{0,0,1,-1},dy[4]{1,-1,0,0};
    void dfs(const vector<vector<char> >&grid,int i,int j)
    {
        vis[i][j] = true;
        for(int k = 0;k<4;k++)
        {
            int x = i+dx[k],y = j+dy[k];
            if(x<0||x>=n||y<0||y>=m||grid[x][y]=='0'||vis[x][y])continue;
            dfs(grid,x,y);
        }
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        n = grid.size(),m = grid[0].size();
        vis.resize(n,vector<bool>(m));
        int ans = 0;
        for(int i = 0;i<n;i++)
        {
            for(int j = 0;j<m;j++)
            {
                if(grid[i][j]=='1'&&vis[i][j]==false)
                {
                    ans++;
                    dfs(grid,i,j);
                }
            }
        }
        return ans;
    }
};
```

## 腐烂的橘子

- 先统计新鲜的橘子的数量，最后如果新鲜的橘子的数量不为0的话，说明橘子无法全部腐烂，这时候返回-1
- 使用一个队列，采用`BFS`的方法，每次向外扩展一层（一层相当于一秒）



```c++
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int n = grid.size(),m = grid[0].size();
        int fresh = 0;
        queue<pair<int,int> >q;
        for(int i = 0;i<n;i++)
        {
            for(int j = 0;j<m;j++)
            {
                if(grid[i][j]==1)fresh++;
                else if(grid[i][j]==2)q.push({i,j});
            }
        }
        int dx[4]{1,-1,0,0},dy[4]{0,0,1,-1};
        int minTime = 0;
        while(!q.empty())
        {
            int sz = q.size();
            bool rotten = false;
            for(int i = 0;i<sz;i++)
            {
                auto t = q.front();
                q.pop();
                for(int k = 0;k<4;k++)
                {
                    int x = t.first+dx[k],y = t.second+dy[k];
                    if(x>=0&&x<n&&y>=0&&y<m&&grid[x][y]==1)
                    {
                        grid[x][y] = 2;
                        q.push({x,y});
                        fresh--;
                        rotten = true;
                    }
                }
            }
            if(rotten)minTime++;
        }
        return fresh?-1:minTime;
    }
};
```

## 课程表

- 一个节点依赖于之前的节点，典型的拓扑排序

```c++
class Solution {
public:
    bool canFinish(int n, vector<vector<int>>& prerequisites) {
        unordered_map<int,vector<int> >edges;
        vector<int>in(n);
        for(auto&e:prerequisites)
        {
            int a = e[0],b = e[1];
            edges[b].push_back(a);
            in[a]++;
        }
        queue<int>q;
        for(int i = 0;i<n;i++)
        {
            if(in[i]==0)
                q.push(i);
        }
        while(!q.empty())
        {
            int t = q.front();
            q.pop();
            for(int&a:edges[t])
            {
                if(--in[a]==0)q.push(a);
            }
        }
        for(int i = 0;i<n;i++)
        {
            if(in[i])return false;
        }
        return true;
    }
};
```

