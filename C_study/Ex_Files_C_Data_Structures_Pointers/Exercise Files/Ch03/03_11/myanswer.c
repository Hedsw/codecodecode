// Create an array of 10 char pointers
// Prompt the user for string input
// Assign each string input to an address stored in the array
// Display the 10 strings input 

// All your code can be part of the main() function; you need not create another function
// collect the string input in a buffer, then copy the text into memory allocated for each array element pointer
// Double pointer (**) notation is not required as part of your solution

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char *strings[10]; 
    char buffer[32];

    for (int i = 0; i < 10; i++) {
        fgets(buffer, 32, stdin);
        strings[i] = (char *)malloc( sizeof(buffer));
        if(strings[i] == NULL) {
            puts("Memory Allocation Failed");
            exit(1);
        }
        printf("Enter your age: \n");
        strcpy(strings[i], buffer);
    }

    printf("Answer\n");
    for (int i = 0; i < 10; i++) {    
        printf("%s", strings[i]);
    }

	return(0);
}
