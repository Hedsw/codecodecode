#include <stdio.h>

int main()
{
	char alpha[] = "abcd";
	char *pa;

	pa = alpha;
	printf("%p\n",pa);
	printf("%p\n",pa+1);

	return(0);
}

