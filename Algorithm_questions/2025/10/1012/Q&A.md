| question                                                     | tag        |
| ------------------------------------------------------------ | ---------- |
| [在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array?envType=study-plan-v2&envId=top-100-liked) | 二分查找   |
| [寻找旋转排序数组中的最小值](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array) | 二分       |
| [搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array?envType=study-plan-v2&envId=top-100-liked) | 二分、数组 |
| [寻找两个有序数组的中位数]()                                 | 二分       |



## 在排序数组中查找元素的第一个和最后一个位置

- 二分查找的板子

```c++
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        if(n==0)return {-1,-1};
        int l = 0,r=n-1;
        while(l<r)
        {
            int mid = l+(r-l)/2;
            if(nums[mid]>=target)r = mid;
            else l = mid+1;
        }
        if(nums[l]!=target)return {-1,-1};
        int temp = l;
        r = n-1;
        while(l<r)
        {
            int mid = l+(r-l+1)/2;
            if(nums[mid]<=target)l = mid;
            else r = mid-1;
        }
        return {temp,r};
    }
};
```

## 寻找旋转排序数组中的最小值

![img](https://i-blog.csdnimg.cn/direct/db170553aac7419ba0810a3078e0d073.png)

- 比B点大的一定位于第一段，比B小的一定位于第二段（二段性）

```c++
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0,right = nums.size()-1;
        int x = nums[right];
        while(left<right)
        {
            int mid = left + (right-left)/2;
            if(nums[mid]>x)left = mid+1;
            else right = mid;
        }
        return nums[left];
    }
};
```



## 搜索旋转排序数组

**核心思想**

把某个数`x`和最后一个数`nums[n-1]`比大小：

- 如果`x>nums[n-1]`，
  - `nums`一定被分成了两个递增段
  - 第一段的所有元素都比第二段的元素大
  - `x`在第一段
- 如果`x<=nums[i]`，那么`x`一定在第二段（或者`nums`是递增数组，只有一段）

```c++
class Solution {
    int findMinIndex(const vector<int>&nums)
    {
        int left = 0,right = nums.size()-1;
        int x = nums[right];
        while(left<right)
        {
            int mid = left+(right-left)/2;
            if(nums[mid]>x)left = mid+1;
            else right = mid;
        }
        return left;
    }
public:
    int search(vector<int>& nums, int target) {
        int i = findMinIndex(nums),n = nums.size();
        int left,right;
        if(target>nums[n-1]){
            // 说明target在第一段,[0,i-1]
            left = 0,right = i-1;
        }else{
            // 说明target在第二段,[i,n-1]
            left = i,right = n-1;
        }
        while(left<right)
        {
            int mid = left+(right-left)/2;
            if(nums[mid]>=target)right = mid;
            else left = mid+1;
        }
        return nums[left]==target?left:-1;
    }
};
```

## 寻找两个有序数组的中位数

1. 问题分析

中位数定义：

- 奇数长度：中间那个数
- 偶数长度：中间两个数的平均值

我们要在两个有序数组中找到合并后的中位数，但不需要真正合并数组。

2. 核心思想

我们在两个数组中找到一条分割线，使得：

- 分割线左边的元素个数 = 分割线右边的元素个数（或比右边多1个）
- 分割线左边的所有元素 ≤ 分割线右边的所有元素

3. 变量定义

- `i`：在 nums1 中的分割位置，表示 nums1[0...i-1] 在左边，nums1[i...m-1] 在右边
- `j`：在 nums2 中的分割位置，表示 nums2[0...j-1] 在左边，nums2[j...n-1] 在右边
- `totalLeft = (m + n + 1) / 2`：左边应有的元素个数

4. 边界条件处理

使用 `INT_MIN` 和 `INT_MAX` 来处理边界情况：

- 当 `i == 0`：nums1 左边没有元素
- 当 `i == m`：nums1 右边没有元素
- 同理处理 nums2

5. 二分查找逻辑

在较短数组 nums1 中进行二分查找：

- 如果 `nums1Left > nums2Right`：说明 nums1 的分割线太靠右，需要向左移动
- 如果 `nums2Left > nums1Right`：说明 nums1 的分割线太靠左，需要向右移动

6. 时间复杂度

- 每次二分查找将搜索范围减半
- 在较短的数组上进行二分，时间复杂度为 O(log(min(m,n)))
- 满足题目要求的 O(log(m+n))

```c++
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if(nums1.size()>nums2.size())return findMedianSortedArrays(nums2,nums1);
        int m = nums1.size(),n = nums2.size();
        int totalLeft = (m+n+1)/2;// 左半部分应该拥有的元素个数
        int left = 0,right = m;
        while(left<=right)
        {
            int i = left + (right-left)/2;
            int j = totalLeft - i;
            int nums1Left = (i == 0) ? INT_MIN : nums1[i - 1];
            int nums1Right = (i == m) ? INT_MAX : nums1[i];
            int nums2Left = (j == 0) ? INT_MIN : nums2[j - 1];
            int nums2Right = (j == n) ? INT_MAX : nums2[j];
            if(nums1Left<=nums2Right&&nums2Left<=nums1Right)
            {
                if((m+n)%2){
                    // 总长是奇数
                    return max(nums1Left,nums2Left);
                }else{
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2.0;
                }
            }else if(nums1Left>nums2Right){
                right = i-1;
            }else{
                left = i+1;
            }
        }
        return 0.0;
    }
};
```

