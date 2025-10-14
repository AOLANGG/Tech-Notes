| question                                                     | tag                  |
| ------------------------------------------------------------ | -------------------- |
| [前k个高频元素](https://leetcode.cn/problems/top-k-frequent-elements?envType=study-plan-v2&envId=top-100-liked) | 小跟堆               |
| [数据流的中位数](https://leetcode.cn/problems/find-median-from-data-stream?envType=study-plan-v2&envId=top-100-liked) | 大、小跟对，中位数   |
| [买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock?envType=study-plan-v2&envId=top-100-liked) | 贪心                 |
| [跳跃游戏](https://leetcode.cn/problems/jump-game?envType=study-plan-v2&envId=top-100-liked) | 贪心                 |
| [跳跃游戏II](https://leetcode.cn/problems/jump-game-ii?envType=study-plan-v2&envId=top-100-liked) | 贪心                 |
| [划分字母区间](https://leetcode.cn/problems/partition-labels?envType=study-plan-v2&envId=top-100-liked) | 贪心、哈希表、双指针 |



## 前k个高频元素

- 看注释即可

```c++
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int>result;
        unordered_map<int,int>cnt;
        for(int&x:nums)
        {
            cnt[x]++;
        }
        // 定义一个小根堆，保留前k个元素，每次插入都pop掉最小的元素，最终保留最大的k个元素
        priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int> >>pq;
        // 遍历频率表，向小根堆中插入元素
        for(auto it=cnt.begin();it!=cnt.end();it++)
        {
            pq.emplace(it->second,it->first);
            if(pq.size()>k)pq.pop();
        }
        // 遍历小根堆的结果
        while(!pq.empty())
        {
            result.emplace_back(pq.top().second);
            pq.pop();
        }
        return result;
    }
};
```

## 买卖股票的最佳时间

- 题目要求——**某一个**买入股票，在**未来的某一个不同的日子**卖出股票
- 只需要维护之前元素的一个最小值，当前元素和它做差，更新结果即可

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 维护一个最小值
        int minVal = INT_MAX,result = 0;
        for(int&x:prices)
        {
            result = max(result,x-minVal);
            // 更新最小值
            minVal = min(minVal,x);
        }
        return result;
    }
};
```

## 跳跃游戏

- 刚开始是在数组的第一个下标，要求我们回答是否可以到达最后一个下标的位置
- 我们维护一个最远可达的位置`cover`，每次遍历一个位置，就更新它最远可达的位置，直到这个位置可以到达最后一个位置（`cover>=nums.size()-1`）或者遍历所有位置结束

```c++
class Solution {
public:
    bool canJump(vector<int>& nums) {
        if(nums.size()==1)return true;
        int cover = 0;
        for(int i = 0;i<=cover;i++)
        {
            cover = max(cover,i+nums[i]);
            if(cover>=nums.size()-1)return true;
        }
        return false;
    }
};
```

## 跳跃游戏II

- 遍历数组（不包括最后一个元素，因为到达最后一个元素即结束）。

- 对于每个位置`i`，更新`farthest`为 “当前`farthest`” 与 “`i + nums[i]`（从`i`能跳到的最远位置）” 的最大值，即追踪当前覆盖范围内的最远可达点。

- 当遍历到`current_end`

  （当前跳跃的覆盖范围终点）时：

  - 说明必须进行一次新的跳跃（因为当前范围内的所有位置已遍历完，下一步需跳到更远的范围），因此`jumps`加 1。
  - 将`current_end`更新为`farthest`（新的覆盖范围终点）。
  - 若新的`current_end`已覆盖最后一个位置（`>=n-1`），直接返回`jumps`（提前结束，无需继续遍历）。

```c++
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if(n==1)return 0;
        int jumps = 0;
        int current_end = 0; // 当前可达的最大距离
        int farthest = 0; // 下一个位置可达的最大距离
        for(int i = 0;i<n-1;i++)
        {
            farthest = max(farthest,i+nums[i]);
            if(i == current_end)
            {
                jumps++;
                current_end = farthest;
                if(current_end>=n-1)return jumps;
            }
        }
        // 一般来说，不会走到这一步，因为题目已经保证了一定有结果
        return -1;
    }
};
```

## 数据流的中位数

```c++
class MedianFinder {
public:
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        if(left.size()==right.size())
        {
            right.push(num);
            left.push(right.top());
            right.pop();
        }
        else
        {
            left.push(num);
            right.push(left.top());
            left.pop();
        }
    }
    
    double findMedian() {
        if(left.size()>right.size())return left.top();
        else return (left.top()+right.top())/2.0;
    }
private:
    // 大根堆
    priority_queue<int>left;
    // 小根堆
    priority_queue<int,vector<int>,greater<int> >right; 
};
```

## 划分字母区间



- **每个字符的最后出现位置决定了片段的边界**
- 如果一个字符在位置 `i` 出现，那么包含该字符的片段至少需要延伸到该字符最后出现的位置

- `left` 记录当前片段的起始位置
- `right` 记录当前片段必须到达的最远位置
- 遍历过程中，对于每个字符 `s[i]`：
  - 更新 `right` 为当前字符最后出现位置和当前 `right` 的较大值
  - 当遍历到 `i == right` 时，说明当前片段包含了所有需要包含的字符，可以安全划分

```c++
class Solution {
public:
    vector<int> partitionLabels(string s) {
        int n = s.size();
        // 记录每个字母出现的最远的位置
        int index[26]{};
        for(int i = 0;i<n;i++)
        {
            index[s[i]-'a'] = i;
        }   
        int left = 0,right = 0;
        vector<int>result;
        for(int i = 0;i<n;i++)
        {
            right = max(right,index[s[i]-'a']);
            if(i == right)
            {
                result.emplace_back(right-left+1);
                left = i+1;
            }
        }
        return result;
    }
};
```

