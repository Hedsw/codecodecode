#include <stdio.h>

int main()
{
	char pet[] = "kat";

	printf("Before: %s\n",pet);
	pet[0] = 'c';
	printf("After: %s\n",pet);

	return(0);
}
