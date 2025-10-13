| question                                                     | tag          |
| ------------------------------------------------------------ | ------------ |
| [有效的括号](https://leetcode.cn/problems/valid-parentheses?envType=study-plan-v2&envId=top-100-liked) | 栈           |
| [最小栈](https://leetcode.cn/problems/min-stack?envType=study-plan-v2&envId=top-100-liked) | 栈、最小前缀 |
| [字符串解码](https://leetcode.cn/problems/decode-string?envType=study-plan-v2&envId=top-100-liked) | 栈           |
| [每日温度](https://leetcode.cn/problems/daily-temperatures?envType=study-plan-v2&envId=top-100-liked) | 单调栈       |
| [柱状图中的最大矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram?envType=study-plan-v2&envId=top-100-liked) | 单调栈       |
| [数组中的第k大的元素](https://leetcode.cn/problems/kth-largest-element-in-an-array?envType=study-plan-v2&envId=top-100-liked) | 快速选择排序 |



## 有效的括号

 一共有三种不符合的条件

1. 左括号多余

2. 右括号多余

3. 左右括号不匹配

```c++
class Solution {
public:
    bool isValid(string s) {
        // 一共有三种不符合的条件
        // 1. 左括号多余
        // 2. 右括号多余
        // 3. 左右括号不匹配
        stack<char>st;
        for(char&c:s)
        {
            if(c=='{')st.push('}');
            else if(c=='(')st.push(')');
            else if(c=='[')st.push(']');
            else if(st.empty()||st.top()!=c)return false;
            else st.pop();
        }
        return st.empty();
    }
};
```

## 最小栈

- 和栈顶之前的数据对应的最小值与当前的插入值做比对，更新当前的最小值；如果栈为空，可以让它返回`INT_MAX`

```c++
class MinStack {
public:
    MinStack() {
    }
    
    void push(int val) {
        st.emplace(val,min(val,getMin()));
    }
    
    void pop() {
        st.pop();
    }
    
    int top() {
        return st.top().first;
    }
    
    int getMin() {
        if(st.empty())return INT_MAX;
        return st.top().second;
    }
private:
    // 当前的值和当前的最小值
    stack<pair<int,int> >st;
};
```

## 字符串解码

1. 遇到数字：提取这个数字加入到“数字栈”中
2. 遇到'['：这说明我们需要把后面的字符串给提取出来
3. 遇到‘]’：这说明提取字符串结束了，解析，然后放到“字符串栈”的栈顶元素的后面
4. 遇到单独的字符：提取出来这个字符串，直接放在“字符串栈顶“元素的后面

```c++
class Solution {
public:
    string decodeString(string s) {
        stack<int>nums;
        stack<string>st;
        st.push("");
        int i = 0,n = s.size();
        while(i<n)
        {
            if(s[i]>='0'&&s[i]<='9')
            {
                int temp = 0;
                while(s[i]>='0'&&s[i]<='9')temp = temp*10+s[i++]-'0';
                nums.push(temp);
            }
            else if(s[i]=='[')
            {
                st.push("");
                i++;
            }
            else if(s[i]==']')
            {
                int cnt = nums.top();
                nums.pop();
                string str = st.top();
                st.pop();
                for(int j = 0;j<cnt;j++)
                    st.top() += str;
                i++;
            }
            else
            {
                st.top()+=s[i++];
            }
        }
        return st.top();
    }
};
```

## 每日温度

**单调栈**

1. 维护一个单调递减的栈（从栈底到栈顶单调递减）
2. 遇到一个比栈顶大的元素，就循环`pop`，直到栈为空或者栈顶比元素大。`pop`的过程中，要更新`result`数组

```c++
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int>result(n);
        stack<pair<int,int> >st;
        for(int i = 0;i<n;i++)
        {
            while(!st.empty()&&st.top().second<temperatures[i])
            {
                auto t = st.top();
                st.pop();
                result[t.first]=i-t.first;
            }
            st.emplace(i,temperatures[i]);
        }
        return result;
    }
};
```

## 柱状图中的最大矩形

- 面积最大的矩形的高度必定是`height`中的元素。假设不是，完全可以增加高度，直到触及某个柱子的顶部

```c++
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int>left(n,-1);
        stack<int>st;
        for(int i = 0;i<n;i++)
        {
            while(!st.empty()&&heights[st.top()]>=heights[i])
            {
                st.pop();
            }
            if(!st.empty())
            {
                left[i]=st.top();
            }
            st.push(i);
        }
        vector<int>right(n,n);
        st = stack<int>();
        for(int i = n-1;i>=0;i--)
        {
            while(!st.empty()&&heights[st.top()]>=heights[i])
            {
                st.pop();
            }
            if(!st.empty())
            {
                right[i]=st.top();
            }
            st.push(i);
        }
        int ans = 0;
        for(int i = 0;i<n;i++)ans = max(ans,heights[i]*(right[i]-left[i]-1));
        return ans;
    }
};
```

## 数组中的第k大的元素

- 挖坑法

```c++
class Solution {
    int QuickSort(vector<int>&a,int left,int right,int target)
    {
        if(left>=right)return a[left];
        int mid = left+right>>1;
        swap(a[left],a[mid]);
        int begin = left,end = right;
        int key = a[begin],pivot = begin;
        while(begin<end)
        {
            while(begin<end&&a[end]>=key)end--;
            a[pivot] = a[end];
            pivot = end;
            while(begin<end&&a[begin]<=key)begin++;
            a[pivot] = a[begin];
            pivot = begin;
        }
        a[pivot] = key;
        if(pivot==target)return a[pivot];
        else if(pivot >= target)return QuickSort(a,left,pivot-1,target);
        else return QuickSort(a,pivot+1,right,target);
    }
public:
    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();
        return QuickSort(nums,0,n-1,n-k);
    }
};
```

