#include <iostream>
#include <cstdio>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(): val(0), next(nullptr) {}
    ListNode(int x): val(x), next(nullptr) {}
    ListNode(int x, ListNode *next): val(x), next(next) {}
};

void push(ListNode** head_ref, int new_data) {
    ListNode* new_node = new ListNode();
    new_node->val = new_data;
    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

void printList(ListNode *node) {
    while(node != NULL) {
        cout << " " << node->val;
        node = node->next;
    } 
}

class Solution {
    public: 
        ListNode* oddEvenList(ListNode* head) {
            if(head == NULL || head->next == NULL)
                return head;
            ListNode* odd = head;
            ListNode* even_head = head->next;
            ListNode* even = even_head;
            
            while(even != NULL && even->next != NULL) {
                odd->next = even->next;
                odd = odd->next;
                even->next = odd->next;
                even = even->next;
            }
            odd->next = even_head;
            return head;
        }
        ListNode* addTwoNumber(ListNode* l1, ListNode* l2) {
            ListNode* l3 = NULL;
            ListNode **node = &l3;
            int sum = 0;
            
            while(l1 != NULL || l2 != NULL || sum >0) {
                if(l1 != NULL) {
                    sum += l1->val;
                    l1 = l1->next;
                }
                if(l2 != NULL) {
                    sum += l2->val;
                    l2 = l2->next;
                }
                *node = new ListNode(sum % 10);
                sum = sum/10;
                node = &((*node)->next);
            }
            return l3;
        }
};

int main() {
    ListNode* head = NULL;
    push(&head, 5);
    push(&head, 4);
    push(&head, 3);
    push(&head, 2);
    push(&head, 1);
    
    Solution A;
    A.oddEvenList(head);
    
    ListNode* l1 = NULL;
    push(&l1, 3);
    push(&l1, 4);
    push(&l1, 2);
    
    ListNode* l2 = NULL;
    push(&l2, 4);
    push(&l2, 6);
    push(&l2, 5);
    
    Solution B;
    ListNode* l3 = B.addTwoNumber(l1, l2);
    printList(l3);
    cout << "Created Linked List is " ;
    printList(head);
    return 0;
 }