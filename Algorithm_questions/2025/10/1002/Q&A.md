| question                                                     | tag    |
| ------------------------------------------------------------ | ------ |
| [除自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self?envType=study-plan-v2&envId=top-100-liked) | 前缀和 |
| [缺失的第一个正数](https://leetcode.cn/problems/first-missing-positive?envType=study-plan-v2&envId=top-100-liked) | 哈希表 |
| [矩阵置零](https://leetcode.cn/problems/set-matrix-zeroes?envType=study-plan-v2&envId=top-100-liked) | 哈希   |
| [螺旋矩阵](https://leetcode.cn/problems/spiral-matrix?envType=study-plan-v2&envId=top-100-liked) | 模拟   |
| [旋转图像](https://leetcode.cn/problems/rotate-image?envType=study-plan-v2&envId=top-100-liked) | 数学   |



## 除自身以外数组的乘积

- 如果知道了 *i* 左边所有数的乘积，以及 *i* 右边所有数的乘积，就可以算出 *answer*[*i*]。

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]

        suf = [1] * n
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        return [p * s for p, s in zip(pre, suf)]
```



## 缺失的第一个正数

- 让数组的第`i`个位置存储数值`i+1`
- 遍历数组，对于每个元素`nums[i]`
- 则将`nums[i]`与`nums[nums[i]-1]`交换
- 交换后，新的`nums[i]`可能还需要继续处理，所以不能直接前进
- 再次遍历数组，找到第一个位置`i`使得`nums[i]~=i+1`
  - 返回`i+1`
- 如果所有的位置都满足`nums[i]=i+1`，返回`n+1`

```cpp
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            while (1 <= nums[i] && nums[i] <= n && nums[i] != nums[nums[i] - 1]) {
                int j = nums[i] - 1;
                swap(nums[i], nums[j]);
            }
        }
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        return n + 1;
    }
};
```

## 矩阵置零

- 标记行和列：首先检查第一行和第一列是否有零，用两个布尔变量来记录一下
- 使用第一行和第一列作为标记：遍历矩阵的其余部分，如果发现某个元素为0，则将该元素对应的第一行和第一列的元素标记成了0
- 根据标记置0：再次遍历矩阵的其余部分，如果第一行或第一列对应元素为0，则将当前元素置零
- 处理第一行和第一列：最后，根据之前记录的布尔变量，决定是否将第一行和第一列全部置零。

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        first_row_zero = any(matrix[0][j]==0 for j in range(n))
        first_col_zero = any(matrix[i][0]==0 for i in range(m))
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row_zero:
            for j in range(n):
                matrix[0][j]=0 
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
```

## 螺旋矩阵

- 初始化四个边界：top=0，bottom=m-1，left=0，right=n-1
- 当top<=bottom且left<=right时循环
  - 从左到右遍历上边界
  - 从上到下遍历右边界
  - 从左到右遍历下边界
  - 从下到上边界左边界
- 每次遍历完一个方向后，调整边界

```cpp
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        top,bottom,left,right = 0,m-1,0,n-1
        result = []
        while top<=bottom and left <= right:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left+=1
        return result
```

## 旋转图像

```cpp
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()
```

