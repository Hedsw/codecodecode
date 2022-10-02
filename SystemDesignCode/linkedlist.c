// Reverse Linked List
struct ListNode {
    int val;
    ListNode *next;
    ListNode(): val(0), next(nullptr) {}
    ListNode(int x): val(x), next(nullptr) {}
    ListNode(int x, ListNode *next): val(x), next(next) {}
};

struct ListNode* reverseList(struct ListNode* head) {
	if(NULL==head) return head;

	struct ListNode *p=head;
	p=head->next;
	head->next=NULL;
	while(NULL!=p){
		struct ListNode *ptmp=p->next;
		p->next=head;
		head=p;
		p=ptmp;
	}
	return head;
}


// Reverse Linked List without Pointers
/*
1. One way is to reverse the data in the nodes without changing the pointers themselves.
2. The second would be to create a new linked list which is a reverse of the original linked list.
*/
struct ListNode* reverseList(struct ListNode* head) {
	if(NULL==head) return head;

	struct ListNode *p=head;
	p=head->next;
	head->next=NULL;
	while(NULL!=p){
		struct ListNode *ptmp=p->next;
		p->next=head;
		head=p;
		p=ptmp;
	}
	return head;
}


// Reverse Linked List between first and last node

typedef struct ListNode node;

struct ListNode* reverseBetween(struct ListNode* head, int m, int n) {
if(head == NULL || head->next == NULL || m == n)
    return head;
    
node *temp = head;
node *start = head;
int i = 1;

while(i < m && temp->next != NULL)
{
    start = temp;
    temp = temp->next;
    i++;
}

node *curr = temp->next;
node *prev = temp;
node *t;
prev->next = NULL;

while(i < n && curr != NULL)
{
    t = curr->next;
    curr->next = prev;
    prev = curr;
    curr = t;
    i++;
}

start->next = prev;
temp->next = curr;

if(m == 1)
    return prev;
return head;
}