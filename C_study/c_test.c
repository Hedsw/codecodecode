#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int makearray(void)
{ 
   int array[5]; // Pointer ㅆㅓ서 넘겨야함
   int x;

   for(x=0; x < 5; x++)
        array[x] = rand() % 10 + 1;
    
    return(array);
}

int main() {
    int x, r[5];

    srand((unsigned)time(NULL));
    r = makearray();
    for(x=0; x < 5; x ++)
        printf("%d \n", r[x]);

    return(0);
}