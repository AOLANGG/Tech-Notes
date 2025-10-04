| question                                                     | tag          |
| ------------------------------------------------------------ | ------------ |
| [删除链表的倒数第N个节点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list?envType=study-plan-v2&envId=top-100-liked) | 链表、双指针 |
| [两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs?envType=study-plan-v2&envId=top-100-liked) | 链表         |
| [K个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group?envType=study-plan-v2&envId=top-100-liked) | 链表         |
| [随机链表的复制](https://leetcode.cn/problems/copy-list-with-random-pointer?envType=study-plan-v2&envId=top-100-liked) | 链表         |
| [排序链表](https://leetcode.cn/problems/sort-list?envType=study-plan-v2&envId=top-100-liked) | 归并排序     |



## 删除链表的倒数第N个节点

- 采用双指针+虚拟头结点的方法
- 先让快指针走`n+1`步，在让快慢指针一起走
- 当快指针走到空位置的时候，慢指针恰好走到要删除节点的前一个位置
- 最后进行删除即可

```c++
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(-1,head);
        ListNode* fast = &dummy,*slow = &dummy;
        for(int i = 0;i<n+1;i++)
            fast = fast->next;
        while(fast){
            fast = fast->next;
            slow = slow->next;
        }
        ListNode* next = slow->next;
        slow->next = next->next;
        delete next;
        return dummy.next;
    }
};
```



## 两两交换链表中的节点

- 使用虚拟头结点的方法

```c++
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0,head);
        ListNode* node0 = &dummy;
        ListNode* node1 = head;
        while(node1&&node1->next){
            ListNode* node2 = node1->next;
            ListNode* node3 = node2->next;
            node0->next = node2;
            node2->next = node1;
            node1->next = node3;
            node0 = node1;
            node1 = node3;
        }
        return dummy.next;
    }
};
```

## K个一组翻转链表

- 纸老虎，做法同[反转链表II](https://leetcode.cn/problems/reverse-linked-list-ii)

```c++
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        // 统计节点的个数
        int n = 0;
        for(ListNode* cur = head;cur;cur=cur->next){
            ++n;
        }
        ListNode dummy(0,head);
        ListNode* p0 = &dummy;
        ListNode* prev = nullptr;
        ListNode* cur = head;
        
        // k 个一组进行处理
        for(;n>=k;n-=k){
            for(int i = 0;i<k;i++){
                ListNode* next = cur->next;
                cur->next = prev;
                prev = cur;
                cur = next;
            }
            ListNode* next = p0->next;
            p0->next->next = cur;
            p0->next = prev;
            p0 = next;
        }
        return dummy.next;
    }
};
```

## 随机链表的复制

```c++
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(head==nullptr)return head;
        for(Node* cur = head;cur;cur=cur->next->next){
            cur->next = new Node(cur->val,cur->next,nullptr);
        }
        for(Node* cur = head;cur;cur=cur->next->next){
            if(cur->random)
                cur->next->random = cur->random->next;
        }
        // 把交错的两个链表分开
        Node* new_head = head->next;
        Node* cur = head;
        for(;cur->next->next;cur = cur->next){
            Node* copy = cur->next;
            cur->next = copy->next;
            copy->next = copy->next->next;
        }
        cur->next=nullptr;
        return new_head;
    }
};
```

## 排序链表

- 缝合怪-找中间节点+合并两个有序链表（归并排序）

```c++
class Solution {
    ListNode* middleNode(ListNode* head) {
        ListNode* pre = head;
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast && fast->next) {
            pre = slow; 
            slow = slow->next;
            fast = fast->next->next;
        }
        pre->next = nullptr; 
        return slow;
    }
    ListNode* mergeTwoLists(ListNode* list1,ListNode* list2){
        ListNode dummy;
        auto cur = &dummy;
        while(list1&&list2){
            if(list1->val<list2->val){
                cur->next = list1;
                list1 = list1->next;
            }else{
                cur->next = list2;
                list2 = list2->next;
            }
            cur = cur->next;
        }
        cur->next = list1?list1:list2;
        return dummy.next;
    }
public:
    ListNode* sortList(ListNode* head) {
        if(head==nullptr||head->next==nullptr)return head;
        ListNode* head2 = middleNode(head);
        head = sortList(head);
        head2  = sortList(head2);
        return mergeTwoLists(head, head2);
    }
};
```

## 合并K个升序链表

- 构造一个最小堆

```c++
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [](const ListNode* a,const ListNode* b){
            return a->val>b->val;// 小根堆
        };
        priority_queue<ListNode*,vector<ListNode*>,decltype(cmp)>pq;
        for(auto head:lists)
            if(head)
                pq.push(head);
        ListNode dummy;
        auto cur = &dummy;
        while(!pq.empty()){
            auto head = pq.top();
            pq.pop();
            if(head->next)pq.push(head->next);
            cur->next = head;
            cur = cur->next;
        }
        return dummy.next;
    }
};
```

