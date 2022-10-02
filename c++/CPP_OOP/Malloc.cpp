// void* malloc(size_t size); 
#include <iostream>
using namespace std;

/*
malloc provides access to a process's heap. 
The heap is a construct in the C core library (commonly libc) that allows objects to obtain 
exclusive access to some space on the process's heap.

Each allocation on the heap is called a heap cell. This typically consists of a header that hold 
information on the size of  the cell as well as a pointer to the next heap cell. 
This makes a heap effectively a linked list.
*/

#define HEAP_START_ADDR (uint32_t)0
#define HEAP_LEN        (uint32_t)10000
#define HEAP_END_ADDR   (uint32_t)(HEAP_START_ADDR + HEAP_LEN - 1)

typedef struct node {
    uint32_t base_add;
    uint32_t len;
    struct node *next;

    node(int b, int l, struct node *n = nullptr) : base_add(b), len(l), next(n) {}
} NODE; 

NODE *Head = nullptr; 

/* Return NULL if memory can not be allocated
* Memory is allocated to first available free slot
*/

void *Malloc(uint32_t size) {
    NODE *p = nullptr;
    if(size != 0) {
        if(Head == nullptr) {
            if(size <= HEAP_LEN) {
                NODE *new_node = new NODE(HEAP_START_ADDR, size, nullptr);
                Head = new_node;
                p = Head; 
                return (void *)(p->base_add);
            }
        }
        else {
            NODE *curr;
            curr = Head;

            // Check if there is any Free space at start of Heap (but before Head) */
            if(curr->base_add != HEAP_START_ADDR) {
                if( (HEAP_START_ADDR + size -1) < curr->base_add) {
                    NODE *new_node = new NODE(HEAP_START_ADDR, size, curr);
                    Head = p = new_node;
                    return (void *)(p->base_add);
                }
            }

            // This is the last node, make sure size is within head limit 
            if ( (curr->base_add + curr->len + size -1) <= HEAP_END_ADDR) {
                NODE *new_node = new NODE(curr->base_add + curr->len, size, curr->next);
                curr->next = p = new_node;

                return (void *)(p->base_add);
            }   
        }
    }

    if(p == nullptr) {
        cout << "Can Not allocate memory size " << size << endl;
    }

    return (void *) p; 
}

// MALLOC을 했으면, FREE도 해야하니까.. FREE 구현..
void Free(void *p) {
    NODE *curr, *prev;

    uint32_t free_addr = (uint32_t) p;
    
    if (Head->base_add == free_addr) {
        curr = Head; // Take back up of Head 
        Head = curr->next; 
        // Delete Head

        delete((NODE *)curr);
        return;
    }
    curr = Head, prev = nullptr;
    while(curr != nullptr) {
        if(curr -> base_add == free_addr) {
            prev->next = curr->next;
            delete((NODE *)curr);
            return;
        }

        prev = curr;
        curr = curr->next;
    }

    cout << "Can not Free Memery" << free_addr << endl; 
}


//다 하고 출력해보고 싶으면.. 이건 굳이 안해도 되지만.. 만약 출력이 필요하다면..
void Print() {
    NODE *curr = Head;
    while(curr != nullptr) {
        cout << curr->base_add << "(" << curr->len  << ")" << " -> ";
        curr = curr->next;
    }
    cout << endl;
}

int main() {
    int *p1 = (int *)Malloc(1000);
    Print();
    int *p2 = (int *)Malloc(2000);
    Print();
    int *p3 = (int *)Malloc(3000);
    Print();
    int *p4 = (int *)Malloc(4000);
    Print();
    int *p5 = (int *)Malloc(5000);
    Print();
    int *p6 = (int *)Malloc(6000);
    Print();

    Free(p1);
    Free(p2);
    Free(p3);
    Free(p4);
    Free(p5);
    Free(p6);

    return 0;
}