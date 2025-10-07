| question                                                     | tag                  |
| ------------------------------------------------------------ | -------------------- |
| [验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree?envType=study-plan-v2&envId=top-100-liked) | 二叉搜索树、中序遍历 |
| [二叉搜索树中第k小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst?envType=study-plan-v2&envId=top-100-liked) | 二叉树               |
| [二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view?envType=study-plan-v2&envId=top-100-liked) | 二叉树、层序遍历     |
| [二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list?envType=study-plan-v2&envId=top-100-liked) | 二叉树、链表         |
| [路径总和III](https://leetcode.cn/problems/path-sum-iii?envType=study-plan-v2&envId=top-100-liked) | 二叉树、哈希表       |



## 验证二叉搜索树

```c++
class Solution {
    long long pre = LLONG_MIN;
public:
    bool isValidBST(TreeNode* root) {
        if(root==nullptr)return true;
        if(!isValidBST(root->left))return false;
        if(root->val<=pre)return false;
        pre = root->val;
        return isValidBST(root->right);
    }
};
```

## 二叉搜索树中第k小的元素

```c++
class Solution {
    int ans = 0;
    void dfs(TreeNode*node,int& k)
    {
        if(node==nullptr || k==0)return;
        dfs(node->left,k);
        if(--k==0)ans = node->val;
        dfs(node->right,k);
    }
public:
    int kthSmallest(TreeNode* root, int k) {
        dfs(root,k);
        return ans;
    }
};
```

## 二叉树的右视图

```c++
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int>result; 
        queue<TreeNode*>q;
        if(root)
            q.push(root);
        while(!q.empty())
        {
            int sz = q.size();
            for(int i = 0;i<sz;i++)
            {
                auto t = q.front();
                q.pop();
                if(i==sz-1)
                {
                    result.push_back(t->val);
                }
                if(t->left)q.push(t->left);
                if(t->right)q.push(t->right);
            }
        }
        return result;
    }
};
```

## 二叉树展开为链表

- 右-左-中的方式遍历这个二叉树
- 头插的方法构建链表

```c++
class Solution {
    TreeNode* head;
public:
    void flatten(TreeNode* root) {
        if(root==nullptr)return;
        flatten(root->right);
        flatten(root->left);
        root->left = nullptr;
        root->right = head;
        head = root;
    }
};
```

## 从前序和中序遍历构造二叉树

```c++
class Solution {
    TreeNode* traversal(const vector<int>& preorder, int l_pre, int r_pre, 
                       const vector<int>& inorder, int l_in, int r_in) {
        // 边界条件：当前子树为空
        if (l_pre > r_pre || l_in > r_in) return nullptr;
        
        // 当前子树的根节点是前序遍历的第一个元素
        int rootValue = preorder[l_pre];
        TreeNode* root = new TreeNode(rootValue);
        
        // 如果只有一个节点，直接返回
        if (l_pre == r_pre) return root;
        
        // 在中序遍历中找到根节点的位置
        int index;
        for (index = l_in; index <= r_in; index++) {
            if (inorder[index] == rootValue) break;
        }
        
        // 计算左子树的节点数量
        int left_size = index - l_in;
        
        // 递归构建左子树
        // 前序遍历中左子树范围：[l_pre+1, l_pre+left_size]
        // 中序遍历中左子树范围：[l_in, index-1]
        root->left = traversal(preorder, l_pre + 1, l_pre + left_size, 
                              inorder, l_in, index - 1);
        
        // 递归构建右子树  
        // 前序遍历中右子树范围：[l_pre+left_size+1, r_pre]
        // 中序遍历中右子树范围：[index+1, r_in]
        root->right = traversal(preorder, l_pre + left_size + 1, r_pre, 
                               inorder, index + 1, r_in);
        
        return root;
    }

public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.empty()) return nullptr;
        return traversal(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }
};
```

## 路径总和III

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int ans = 0;
    unordered_map<long long,int>cnt{{0,1}};
    void dfs(TreeNode* node,long long s,const int&targetSum)
    {
        if(node==nullptr)return;
        s += node->val;
        ans += cnt[s-targetSum];
        cnt[s]++;
        dfs(node->left,s,targetSum);
        dfs(node->right,s,targetSum);
        cnt[s]--;
    }
public:
    int pathSum(TreeNode* root, int targetSum) {
        dfs(root,0,targetSum);
        return ans;
    }
};
```

