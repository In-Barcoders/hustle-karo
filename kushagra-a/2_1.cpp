/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *forward, *behind, *prev;;
        forward =head;
        ListNode *node = new ListNode(-1);
        node->next = head;
        behind = prev = node;
        int count=0;
        while(forward)
        {
            forward = forward->next;
            count++;
            if(count>=n)       
            {
                prev = behind;
                behind = behind->next;
            }
        }
        if(prev->next == head)      
            head = behind->next;
        prev->next = behind->next;

        return head;
    }
};