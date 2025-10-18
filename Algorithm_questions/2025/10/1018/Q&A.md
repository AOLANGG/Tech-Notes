| question                                                     | tag        |
| ------------------------------------------------------------ | ---------- |
| [只出现一次的数字](https://leetcode.cn/problems/single-number?envType=study-plan-v2&envId=top-100-liked) | 异或的性质 |
| [多数元素](https://leetcode.cn/problems/majority-element?envType=study-plan-v2&envId=top-100-liked) | 摩根投票   |
| [颜色分类](https://leetcode.cn/problems/sort-colors?envType=study-plan-v2&envId=top-100-liked) | 双指针     |
| [寻找重复数](https://leetcode.cn/problems/find-the-duplicate-number?envType=study-plan-v2&envId=top-100-liked) | 环形链表   |
| [下一个排列](https://leetcode.cn/problems/next-permutation?envType=study-plan-v2&envId=top-100-liked) | 双指针     |



## 只出现一次的数字

```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for(int&v:nums)
            ans ^= v;
        return ans;
    }
};
```

## 多数元素

```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0,count = 0;
        for(int&x:nums){
            if(count==0)candidate = x;
            count += (candidate==x)?1:-1;
        }
        return candidate;
    }
};
```



```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0,count = 0;
        for(int&x:nums){
            if(count==0)candidate = x;
            count += (candidate==x)?1:-1;
        }
        return candidate;
    }
};
```

## 颜色分类

- 按照双指针的思想，遍历两边数组即可

```c++
class Solution {
public:
    void sortColors(vector<int>& nums) {
        // 可以遍历两遍数组
        int n = nums.size();
        int l = 0,r = n-1;
        while(l<r)
        {
            // 右边找0
            while(l<r&&nums[r]!=0)r--;
            // 左边找非0
            while(l<r&&nums[l]==0)l++;
            if(l<r)swap(nums[l],nums[r]);
        }
        l=0,r = n-1;
        while(l<r)
        {
            // 右边找1
            while(l<r&&nums[r]!=1)r--;
            // 左边找2
            while(l<r&&nums[l]!=2)l++;
            if(l<r)swap(nums[l],nums[r]);
        }
    }
};
```

## 寻找重复数

- 等同于环形链表找入口节点

大概就是这样

![img](https://i-blog.csdnimg.cn/direct/03ef0ee416f54d3ebb0fbfd348f894b4.png)

```c++
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int fast = 0,slow = 0;
        while(true){
            fast = nums[nums[fast]];
            slow = nums[slow];
            if(fast==slow)break;
        }
        int head = 0;
        while(slow!=head){
            head = nums[head];
            slow = nums[slow];
        }
        return slow;
    }
};
```

## 下一个排列

1. **找下降点**：从右向左找到第一个 `nums[i] < nums[i+1]` 的位置 `i`
2. **找交换点**：在下降点右侧找到**大于 nums[i] 的最小数字**进行交换
3. **反转右侧**：将交换点后的部分**反转**，使其变为最小排列（升序）

```c++
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        // 从右向左找到第一个下降点
        int i = n-2;
        while(i>=0&&nums[i]>=nums[i+1])i--;
        if(i>=0){
            int j = n-1;
            while(j>=0&&nums[j]<=nums[i])
                j--;
            swap(nums[i],nums[j]);
        }
        reverse(nums.begin()+i+1,nums.end());
    }
};
```

