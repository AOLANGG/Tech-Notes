| question                                                     | tag                        |
| ------------------------------------------------------------ | -------------------------- |
| [LRU缓存]()                                                  | 链表、哈希表               |
| [二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal?envType=study-plan-v2&envId=top-100-liked) | 二叉树、栈                 |
| [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree?envType=study-plan-v2&envId=top-100-liked) | 二叉树                     |
| [反转二叉树](https://leetcode.cn/problems/invert-binary-tree?envType=study-plan-v2&envId=top-100-liked) | 二叉树                     |
| [对称二叉树](https://leetcode.cn/problems/symmetric-tree?envType=study-plan-v2&envId=top-100-liked) | 二叉树、递归               |
| [二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree?envType=study-plan-v2&envId=top-100-liked) | 二叉树、深度优先搜索       |
| [二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal?envType=study-plan-v2&envId=top-100-liked) | 二叉树，队列，宽度优先搜索 |
| [将有序数组转换成二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree?envType=study-plan-v2&envId=top-100-liked) | 二叉树、分治               |



## LRU缓存

- `splice`是把一个节点移动到另一个位置

```c++
class LRUCache {
    typedef list<pair<int,int>>::iterator LtIter;
public:
    LRUCache(int capacity) {
        _capacity=capacity;
    }
    
    int get(int key) {
        auto ret = _hashMap.find(key);
        if(ret!=_hashMap.end()){
            // 更新key对应的值的位置
            LtIter it = ret->second;
            _LRUList.splice(_LRUList.begin(),_LRUList,it);
            return ret->second->second;
        }
        return -1;
    }
    
    void put(int key, int value) {
        
        auto ret = _hashMap.find(key);
        // 1. 新增
        if(ret==_hashMap.end())
        {
            // 如果满了
            if(_capacity == _hashMap.size())
            {
                auto back = _LRUList.back();
                _hashMap.erase(back.first);
                _LRUList.pop_back();
            }
            _LRUList.push_front(make_pair(key,value));
            _hashMap[key]=_LRUList.begin();
        }
        // 2. 更新
        else
        {
            LtIter it = ret->second;
            it->second = value;
            _LRUList.splice(_LRUList.begin(),_LRUList,it);
        }
    }
private:
    // 查找和更新都是O(1)
    unordered_map<int,LtIter> _hashMap;
    // LRU 假设尾部的数据是最近最少使用的
    list<pair<int,int> >_LRUList;
    size_t _capacity;
};
```



## 二叉树的中序遍历

**非递归版本**

- 先是一路向左，边向左边旺栈中添加节点
- 遇到空，则回退到栈顶的节点，在向右，之后在重复之前的操作

```c++
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int>result;
        auto cur = root;
        stack<TreeNode*> st;
        while(cur||!st.empty())
        {
            if(cur)
            {
                st.push(cur);
                cur = cur->left;
            }
            else
            {
                cur = st.top();
                st.pop();
                result.push_back(cur->val);
                cur = cur->right;
            }
        }        
        return result;
    }
};
```

## 二叉树的最大深度

```c++
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root==nullptr)return 0;
        return max(maxDepth(root->left),maxDepth(root->right))+1;
    }
};
```

## 翻转二叉树

```c++
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root==nullptr)return nullptr;
        invertTree(root->left);
        invertTree(root->right);
        swap(root->left,root->right);
        return root;
    }
};
```

## 对称二叉树

```c++
class Solution {
    bool isSameTree(TreeNode* p,TreeNode* q)
    {
        if(p==nullptr || q == nullptr)return p==q;
        return p->val==q->val && isSameTree(p->left,q->right) && isSameTree(p->right,q->left);
    }
public:
    bool isSymmetric(TreeNode* root) {
        return isSameTree(root->left,root->right);
    }
};
```

## 二叉树的直径

```c++
class Solution {
    int ans = 0;
    int dfs(TreeNode* node)
    {
        if(node == nullptr)return -1;
        int l_len = dfs(node->left),r_len = dfs(node->right);
        ans = max(ans,l_len+r_len+2);
        return max(l_len,r_len)+1;
    }
public:
    int diameterOfBinaryTree(TreeNode* root) {
        dfs(root);
        return ans;
    }
};
```

## 二叉树的层序遍历

```c++
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int> >result;
        queue<TreeNode*>q;
        if(root)
            q.push(root);
        while(!q.empty()){
            int sz = q.size();
            vector<int>temp;
            for(int i = 0;i<sz;i++){
                auto t = q.front();
                q.pop();
                temp.push_back(t->val);
                if(t->left)q.push(t->left);
                if(t->right)q.push(t->right);
            }
            result.push_back(temp);
        }
        return result;
    }
};
```

## 将有序数组转换为二叉搜索树

```c++
class Solution {
    TreeNode* dfs(const vector<int>&nums,int l,int r)
    {
        if(l>r)return nullptr;
        int mid = (l+r)/2;
        TreeNode* root = new TreeNode(nums[mid]);
        if(l==r)
        {
            return root;
        }
        root->left = dfs(nums,l,mid-1);
        root->right = dfs(nums,mid+1,r);
        return root;
    }
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return dfs(nums,0,nums.size()-1);
    }
};
```

