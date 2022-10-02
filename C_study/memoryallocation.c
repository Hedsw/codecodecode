#include <stdlib.h>
#include <stdio.h>

int main (int argc, char* argv[]) {
    int number_count = 4;

    int* my_number_ptr = (int*)malloc(number_count * sizeof(int));
    printf("Address of malloc'd block of memery %p \n", my_number_ptr);

    for(int i = 0; i < number_count; i++) {
        *(my_number_ptr + i) = i;
        printf("Added value %d to address %p \n", i, my_number_ptr + i);
    }

    print("\n\n");

    return 0;
}