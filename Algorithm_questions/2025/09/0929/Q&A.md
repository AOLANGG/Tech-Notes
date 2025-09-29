| question                                                     | tag              |
| ------------------------------------------------------------ | ---------------- |
| [接雨水](https://leetcode.cn/problems/trapping-rain-water?envType=study-plan-v2&envId=top-100-liked) | 动态规划、双指针 |
| [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters?envType=study-plan-v2&envId=top-100-liked) | 滑动窗口         |
| [找到字符串中所有字母易位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string?envType=study-plan-v2&envId=top-100-liked) | 滑动窗口         |

## 接雨水

### 动态规划

- 对于每个位置，它能接的雨水量 = min(左边最高墙, 右边最高墙) - 当前高度
- 提前计算好每个位置的左右最大值，避免重复计算

**代码**

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int>prev(n);
        auto bak = prev;
        prev[0] = height[0];
        for(int i = 1;i<n;i++)
        {
            prev[i] = max(prev[i-1],height[i]);
        }
        bak[n-1] = height[n-1];
        for(int i = n-2;i>=0;i--)
        {
            bak[i] = max(bak[i+1],height[i]);
        }
        int ans = 0;
        for(int i = 0;i<n;i++)
        {
            ans+=min(prev[i],bak[i])-height[i];
        }
        return ans;
    }
};
```

### 双指针

- 左右指针从两端向中间移动，"谁小谁动"，这样可以保证最后一定能移动到最大的高度
- 遍历的过程中处理一下结果

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = pre_max = suf_max = 0
        left,right = 0,len(height)-1
        while left<right:
            pre_max = max(pre_max,height[left])
            suf_max = max(suf_max,height[right])
            if pre_max < suf_max:
                ans += pre_max-height[left]
                left+=1
            else:
                ans += suf_max-height[right]
                right-=1
        return ans
```

## 无重复字符的最长子串

### 滑动窗口

- 检验一个窗口是否合格，合格的话，需要更新结果，否则对窗口进行滑动

- 流程：进窗口，出窗口，更新结果

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        int vis[128];
        auto check = [&vis]()->bool{
            for(int i = 0;i<128;i++){
                if(vis[i]>1)return false;
            }
            return true;
        };
        int ans = 0;
        for(int left = 0,right = 0;right<n;right++){
            vis[s[right]]++;
            while(!check()){
                vis[s[left++]]--;
            }
            ans = max(ans,right-left+1);
        }
        return ans;
    }
};
```

## 找到字符串中所有字母易位词

## 滑动窗口

- 维护一个长为 **len(p)** 的子串，判断其中出现的字母的个数是否和p中出现的字母相同即可

```
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int>result;
        int n = s.size();
        int cnt_s[26]{},cnt_p[26]{};
        for(char&c:p)
            cnt_p[c-'a']++;
        auto check = [&cnt_s,&cnt_p](){
            for(int i = 0;i<26;i++){
                if(cnt_s[i]!=cnt_p[i])return false;
            }
            return true;
        };
        for(int right = 0;right<n;right++){
            cnt_s[s[right]-'a']++;
            int left = right-p.size()+1;
            if(left<0)continue;
            if(check()){
                result.push_back(left);
            }
            cnt_s[s[left]-'a']--;
        }
        return result;
    }
};
```



