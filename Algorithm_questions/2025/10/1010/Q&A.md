| question                                                     | tag        |
| ------------------------------------------------------------ | ---------- |
| [实现Trie（前缀树）](https://leetcode.cn/problems/implement-trie-prefix-tree?envType=study-plan-v2&envId=top-100-liked) | 字典树     |
| [全排列](https://leetcode.cn/problems/permutations?envType=study-plan-v2&envId=top-100-liked) | 暴搜       |
| [子集](https://leetcode.cn/problems/subsets?envType=study-plan-v2&envId=top-100-liked) | 搜索、回溯 |
| [电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number?envType=study-plan-v2&envId=top-100-liked) | 搜索       |



## 实现Trie（前缀树）

- 26叉树罢了

```c++
struct Node
{
    Node* son[26]{};
    bool end = false;
};
class Trie {
public:
    Trie():
        root(new Node())
    {
        
    }
    ~Trie()
    {
        destory(root);
    }
    void insert(string word) {
        Node* cur = root;
        for(char&c:word)
        {
            c-='a';
            if(cur->son[c]==nullptr)
                cur->son[c] = new Node();
            cur = cur->son[c];
        }
        cur->end = true;
    }
    
    bool search(string word) {
        return find(word)==2;
    }
    
    bool startsWith(string prefix) {
        return find(prefix)!=0;
    }
private:
    int find(string word)
    {
        Node* cur = root;
        for(char&c:word)
        {
            c-='a';
            if(cur->son[c]==nullptr)return 0;
            cur = cur->son[c];
        }
        return cur->end?2:1;
    }
    void destory(Node* node)
    {
        if(node==nullptr)return;
        for(Node* son:node->son)
            destory(son);
        delete node;
        node = nullptr;
    }
private:
    Node* root;
};
```

## 全排列

```c++
class Solution {
    vector<vector<int> >result;
    vector<bool>vis;
    vector<int>path;
    int n;
    void dfs(const vector<int>& nums,int u)
    {
        if(u==n)
        {
            result.push_back(path);
            return;
        }
        for(int i = 0;i<n;i++)
        {
            if(!vis[i])
            {
                path.push_back(nums[i]);
                vis[i] = true;
                dfs(nums,u+1);
                path.pop_back();
                vis[i] = false;
            }
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        n = nums.size();
        vis.resize(n);
        dfs(nums,0);
        return result;
    }
};
```

## 子集

- 根据 当前的数选择或者不选择 来进行搜索

```c++
class Solution {
    vector<vector<int> >result;
    vector<int>path;
    void dfs(const vector<int>& nums,int u)
    {
        if(u == nums.size())
        {
            result.push_back(path);
            return;
        }
        path.push_back(nums[u]);
        dfs(nums,u+1);
        path.pop_back();
        dfs(nums,u+1);
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        dfs(nums,0);
        return result;
    }
};
```

## 电话号码的字母组合

```c++
class Solution {
    string str[10]={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    string path;
    vector<string>result;
    void dfs(const string& digits,int u)
    {
        if(u==digits.size())
        {
            result.push_back(path);
            return;
        }
        for(char& c:str[digits[u]-'0'])
        {
            path.push_back(c);
            dfs(digits,u+1);
            path.pop_back();
        }
    }
public:
    vector<string> letterCombinations(string digits) {
        if(digits.empty())return result;
        dfs(digits,0);
        return result;
    }
};
```

