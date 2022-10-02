// Sparse Matrix - 희소행렬
/*
Sparse Matrix를 사용하는 이유 
저장소: 0보다 0이 아닌 요소가 더 적으므로 해당 요소만 저장하는 데 더 적은 메모리를 사용할 수 있습니다.
계산 시간: 0이 아닌 요소만 순회하는 데이터 구조를 논리적으로 설계하여 계산 시간을 절약할 수 있습니다.

희소행렬은 2개의 방법으로 표현 가능함.
1. Array Representation
2. Linked List Representation.

*/    
/*
        Row, Col, Value
0 0 0    1    1    1
0 1 0 -> 0    2    5
5 0 3    2    2    3 
이런식으로 변경 시키는 거
*/
// Using Array...
/*
3가지 구성요소..
Row: Index of row, where non-zero element is located
Column: Index of column, where non-zero element is located
Value: Value of the non zero element located at index – (row,column)
*/
#include <iostream>
using namespace std;
 
int main()
{
    // Assume 4x5 sparse matrix
    int sparseMatrix[4][5] =
    {
        {0 , 0 , 3 , 0 , 4 },
        {0 , 0 , 5 , 7 , 0 },
        {0 , 0 , 0 , 0 , 0 },
        {0 , 2 , 6 , 0 , 0 }
    };
 
    int size = 0;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 5; j++)
            if (sparseMatrix[i][j] != 0)
                size++;
 
    // number of columns in compactMatrix (size) must be
    // equal to number of non - zero elements in
    // sparseMatrix
    int compactMatrix[3][size];
 
    // Making of new matrix
    int k = 0;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 5; j++)
            if (sparseMatrix[i][j] != 0)
            {
                compactMatrix[0][k] = i;
                compactMatrix[1][k] = j;
                compactMatrix[2][k] = sparseMatrix[i][j];
                k++;
            }
 
    for (int i=0; i<3; i++)
    {
        for (int j=0; j<size; j++)
            cout <<" "<< compactMatrix[i][j];
 
        cout <<"\n";
    }
    return 0;
}

// Using Linked List 
/*
4가지 구성요소..
Row: Index of row, where non-zero element is located
Column: Index of column, where non-zero element is located
Value: Value of the non zero element located at index – (row,column)
Next node: Address of the next node
*/
// C++ program for sparse matrix representation.
// Using Link list
// Time Complexity -> O(1) 
#include<iostream>
using namespace std;
 
// Node class to represent link list
class Node
{
    public:
    int row;
    int col;
    int data;
    Node *next;
};
 
// Function to create new node
void create_new_node(Node **p, int row_index,
                     int col_index, int x)
{
    Node *temp = *p;
    Node *r;
     
    // If link list is empty then
    // create first node and assign value.
    if (temp == NULL)
    {
        temp = new Node();
        temp->row = row_index;
        temp->col = col_index;
        temp->data = x;
        temp->next = NULL;
        *p = temp;
    }
     
    // If link list is already created
    // then append newly created node
    else
    {
        while (temp->next != NULL)  
            temp = temp->next;
             
        r = new Node();
        r->row = row_index;
        r->col = col_index;
        r->data = x;
        r->next = NULL;
        temp->next = r;
    }
}
 
// Function prints contents of linked list
// starting from start
void printList(Node *start)
{
    Node *ptr = start;
    cout << "row_position:";
    while (ptr != NULL)
    {
        cout << ptr->row << " ";
        ptr = ptr->next;
    }
    cout << endl;
    cout << "column_position:";
 
    ptr = start;
    while (ptr != NULL)
    {
        cout << ptr->col << " ";
        ptr = ptr->next;
    }
    cout << endl;
    cout << "Value:";
    ptr = start;
     
    while (ptr != NULL)
    {
        cout << ptr->data << " ";
        ptr = ptr->next;
    }
}
 
// Driver Code
int main()
{
     
    // 4x5 sparse matrix
    int sparseMatrix[4][5] = { { 0 , 0 , 3 , 0 , 4 },
                               { 0 , 0 , 5 , 7 , 0 },
                               { 0 , 0 , 0 , 0 , 0 },
                               { 0 , 2 , 6 , 0 , 0 } };
     
    // Creating head/first node of list as NULL
    Node *first = NULL;
    for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 5; j++)
        {
             
            // Pass only those values which
            // are non - zero
            if (sparseMatrix[i][j] != 0)
                create_new_node(&first, i, j,
                                sparseMatrix[i][j]);
        }
    }
    printList(first);
 
    return 0;
}