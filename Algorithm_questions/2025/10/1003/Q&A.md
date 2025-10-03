| question                                                     | tag            |
| ------------------------------------------------------------ | -------------- |
| [搜索二维矩阵 II](https://leetcode.cn/problems/search-a-2d-matrix-ii?envType=study-plan-v2&envId=top-100-liked) | 数组           |
| [相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists?envType=study-plan-v2&envId=top-100-liked) | 链表、双指针   |
| [反转链表](https://leetcode.cn/problems/reverse-linked-list?envType=study-plan-v2&envId=top-100-liked) | 链表           |
| [回文链表](https://leetcode.cn/problems/palindrome-linked-list?envType=study-plan-v2&envId=top-100-liked) | 链表、双指针   |
| [环形链表](https://leetcode.cn/problems/linked-list-cycle?envType=study-plan-v2&envId=top-100-liked) | 链表、快慢指针 |
| [环形链表II](https://leetcode.cn/problems/linked-list-cycle-ii?envType=study-plan-v2&envId=top-100-liked) | 双指针         |
| [合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists?envType=study-plan-v2&envId=top-100-liked) | 链表           |
| [两数相加](https://leetcode.cn/problems/add-two-numbers?envType=study-plan-v2&envId=top-100-liked) | 链表           |



## 搜索二维矩阵 II

- 利用矩阵有序的特性，从**右上角**（或者左下角也可以）开始遍历
- 如果当前值比目标值大，就让`col-=1`
- 如果当前及比目标值小，就让`row+=1`

```c++
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // 从右上角或者左下角开始遍历，因为这样可以进行夹逼
        int m = matrix.size(),n = matrix[0].size();
        int row = 0,col = n-1;
        while(row<m&&col>=0){
            if(matrix[row][col]==target)return true;
            else if(matrix[row][col]>target)col--;
            else row++;
        }
        return false;
    }
};
```



## 相交链表

- 假设链表A独有的长度是a，链表B独有的长度是b，它们共有的长度是c
- 要找到公共的节点的开始，只需要用两个指针：
  - 指针1，先遍历整个链表A，在遍历链表B
  - 指针2，先遍历整个链表B，在遍历链表A
  - 两个指针同时开始遍历
- 如果中间两个指针相等了，就说明找到了公共节点的开始

```c++
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* cur1 = headA,*cur2 = headB;
        bool flag1 = true,flag2 = true;
        while(cur1&&cur2){
            if(cur1==cur2)return cur1;
            cur1=cur1->next;
            cur2=cur2->next;
            if(cur1==nullptr&&flag1){
                flag1 = false;
                cur1 = headB;
            }
            if(cur2==nullptr&&flag2){
                flag2 = false;
                cur2 = headA;
            }
        }
        return nullptr;
    }
};
```



## 反转链表

- 比较简单，不过面试应该考的比较多，这里多研究几种做法

### 虚拟头结点

```c++
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* dummy = new ListNode(-1);
        while(head){
            ListNode* next = head->next;
            head->next = dummy->next;
            dummy->next = head;
            head = next;
        }
        head = dummy->next;
        delete dummy;
        return head;
    }
};
```



### 三指针遍历(瞎起的名字)

```c++
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr,*cur = head;
        while(cur)
        {
            ListNode* next = cur->next;
            cur->next=prev;
            prev=cur;
            cur=next;
        }
        return prev;
    }
};
```

## 回文链表

- 首先找到链表的中间节点
  - 如果链表是奇数个节点，找正中间的节点
  - 如果链表是偶数个节点，找正中间右边的节点
- 然后把中间节点到链表末尾反转
- 最后，同时遍历`head`和`head2`这两个链表

```c++
class Solution {
    ListNode* middleNode(ListNode* head){
        ListNode* fast = head,*slow = head;
        while(fast&&fast->next){
            fast=fast->next->next;
            slow=slow->next;
        }
        return slow;
    }
    ListNode* reverseList(ListNode* head){
        ListNode* prev = nullptr;
        ListNode* cur = head;
        while(cur){
            ListNode* next = cur->next;
            cur->next=prev;
            prev=cur;
            cur=next;
        }
        return prev;
    }
public:
    bool isPalindrome(ListNode* head) {
        ListNode* mid = middleNode(head);
        ListNode* head2 = reverseList(mid);
        while(head2)
        {
            if(head->val!=head2->val)return false;
            head=head->next;
            head2=head2->next;
        }
        return true;
    }
};
```



## 环形链表

原理：

- 快指针，每次都比慢指针多走一步，如果是存在环的链表，那么只要快指针比慢指针多走n圈，两个指针就能相遇，这就能说明存在环
- 相反，如果不存在环，那么快指针就会先走到空节点，这时候直接返回`false`就行了

```c++
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* fast = head,*slow = head;
        while(fast&&fast->next){
            fast=fast->next->next;
            slow=slow->next;
            if(fast==slow)return true;
        }
        return false;
    }
};
```



环形链表II

- 首先来判断一下是否是正在存在环，不存在的话就返回`nullptr`
- 让慢指针和头指针同时开始走，它们相遇的地方就是环的入口

证明：
假设进环之前的路程为`a`，环长为`b`设慢指针走了x步时，快门指针相遇，此时快指针走了`2x`步，并且快指针比慢指针多走了n圈，即`2x-x=x=nb`，也就是说慢指针总共走过的路程是`nb`。不过，在这`nb`中，实际上包含了进环钱的一个`a`，所以只需要让慢指针在走`a`步，就可以到达环的入口。

```c++
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* fast = head,*slow = head;
        while(fast&&fast->next){
            fast = fast->next->next;
            slow = slow->next;
            if(fast==slow){
                while(head!=slow){
                    head = head->next;
                    slow = slow->next;
                }
                return head;
            }
        }
        return nullptr;
    }
};
```



## 合并两个有序链表



### 哨兵位

```c++
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode(-1);
        auto cur = dummy;
        while(list1&&list2){
            if(list1->val<list2->val){
                cur->next = list1;
                cur = list1;
                list1 = list1->next;
            }else{
                cur->next = list2;
                cur=list2;
                list2 = list2->next;
            }
        }
        if(list1)
            cur->next = list1;
        if(list2)
            cur->next = list2;
        ListNode* head = dummy->next;
        delete dummy;
        return head;
    }
};
```

### 递归

```c++
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1==nullptr)return list2;
        if(list2==nullptr)return list1;
        if(list1->val<list2->val){
            list1->next = mergeTwoLists(list1->next,list2);
            return list1;
        }
        list2->next=mergeTwoLists(list1,list2->next);
        return list2;
    }
};
```

## 两数相加

```c++
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy;
        ListNode* cur = &dummy;
        int carry = 0;
        while(l1||l2||carry){
            if(l1){
                carry+=l1->val;
                l1 = l1->next;
            }
            if(l2){
                carry += l2->val;
                l2 = l2->next;
            }
            cur->next = new ListNode(carry%10);
            cur = cur->next;
            carry/=10;
        }
        return dummy.next;
    }
};
```

